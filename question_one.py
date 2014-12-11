# Question 1:
# Please write a small handful of Selenium tests in Python against http://www.moat.com:

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import requests

browser = webdriver.Chrome() # get local session of chrome
browser.get("http://www.moat.com") #load page


# 1.  Verify that the "Try These" links are random and that they work.
links =

# 2.  Verify that the "Recently Seen Ads" are no more than half an hour old.

# 3.  Verify that the ad counts are correct, even when they are over 100.

# 4.  Verify the "Share this Ad" feature.
