import requests
import time
from bs4 import BeautifulSoup
import RPi.GPIO as GPIO
import spidev
from lib_nrf24 import NRF24
import WebScraper


def setupRadio(radio, radioAddress):
    radio.begin(0, 25)
    radio.openWritingPipe(radioAddress)
    radio.setChannel(0x77)
    radio.setPALevel(NRF24.PA_MAX)
    radio.enableDynamicPayloads()
    radio.stopListening();
    radio.setPayloadSize(32)
    radio.setDataRate(NRF24.BR_1MBPS)
    radio.setAutoAck(False);
    radio.enableAckPayload()
    radio.printDetails()
    print('Radio should be set up')
    


if __name__ == '__main__':
    
    # prepare GPIO pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    # Set up Radio Transmitter
    radioAddress = [0xe8, 0xe8, 0xf0, 0xf0, 0xe1]
    radio = NRF24(GPIO, spidev.SpiDev())
    setupRadio(radio, radioAddress)
    
    # Get commands and send them
    while True:
        command = WebScraper.getCommand()
        if command == 'turn left':
            message = 'll'
        elif command == 'turn right':
            message = 'rr'
        elif command == 'forwards':
            message = 'ff'
        elif command == 'backwards':
            message = 'bb'
        else:
            message = 'ss';
        radio.write(message)
        print('message sent')
        time.sleep(.05)
    
    
    GPIO.cleanup()