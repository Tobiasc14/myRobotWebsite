# myRobotWebsite

My Robot Website
====================

This is a project where I created a website using Django and hosted on heroku to remote control an arduino based robot.
The website updates commands in a database based on which button the user pushes. A Rasberry pi then scrapes this website 
and reads which command is currently being displayed. It then transmits the command information to the arduino using an NRF24L01
Based on the commands received, the arduino code then sends power to specific ports of a motor controller to turn the motors
on and off