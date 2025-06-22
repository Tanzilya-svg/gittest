from sys import executable
import time
import selenium

print('version', selenium.__version__)

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
while(True):
       pass
