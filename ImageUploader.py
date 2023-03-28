from selenium import webdriver
import time

# Set up the webdriver
browser = webdriver.Chrome()

# Go to the website URL
url = "http://24.218.29.129/robincam/"
browser.get(url)

# Find the file input element and send the image file path to it
file_input = browser.find_element(by='name', value='picture')
file_path = "C:/Users/hjctj/PycharmProjects/myRobotWebsite/PlanetSkyline.png"
file_input.send_keys(file_path)

# Submit the form
submit_button = browser.find_element(by='xpath', value="//button[@type='submit']")
submit_button.click()

# Wait for the page to load
time.sleep(5)

# Close the browser
browser.quit()
