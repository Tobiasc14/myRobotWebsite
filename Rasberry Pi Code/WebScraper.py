import requests
import time
from bs4 import BeautifulSoup
import RPi.GPIO as GPIO


def getCommand():
    website = requests.get("http://my-robot-website.herokuapp.com/ready").text
    webInfo = BeautifulSoup(website, 'html.parser')
    command = webInfo.find('div', class_='command')

    if (command.text.strip() == ''):
        #print('stop')
        return 'stop'

    else:
        #print(command.text.strip())
        return command.text.strip()
        
if __name__ == '__main__':
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    
    while True:
        command = getCommand()
        print(command)
        if command == 'stop':
            pass
            #GPIO.output(18, GPIO.LOW)
        else:
            #GPIO.output(18, GPIO.HIGH)
            pass
        time.sleep(.05)
        
    



