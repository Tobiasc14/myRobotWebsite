from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Set up the webdriver
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium-browser'
service = Service('/usr/lib/chromium-browser/chromedriver')
browser = webdriver.Chrome(service = service, options=options)

# Go to the website URL
url = "http://24.218.29.129/robincam/"
browser.get(url)

# Find the file input element and send the image file path to it
file_input = browser.find_element(by='name', value='picture')
file_path = "/home/pi/Pictures/Screenshot.png"
file_input.send_keys(file_path)
time.sleep(2)

# Submit the form
submit_button = browser.find_element(by='xpath', value="//button[@type='submit']")
submit_button.click()

# Wait for the page to load
time.sleep(3)
# Close the browser
browser.quit()
