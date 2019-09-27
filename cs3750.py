#Mei-Ying Croddy 
#CS3750-01

# we are using a specific webdriver and tool called Selenium. You need Selenium in order to make this program work.
from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

#I have installed the Firefox webdriver on my own computer. 
browser = webdriver.Firefox()
#This command simply opens up google.com in the chosen browser (Firefox in this case).
browser.get('http://www.google.com')
time.sleep(1.5)

#this code looks for an element on the page labelled 'q' in this case.
search = browser.find_element_by_name('q')

#I set the query to be something innocuous. This value is written into the search bar.
search.send_keys("cute rabbit images")
#This code simulates hitting the return key on the keyboard, thus activating the search.
search.send_keys(Keys.RETURN)

