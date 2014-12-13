

# import selenium
# import sys
# import unittest

# Question 1:
# Please write a small handful of Selenium tests in Python against http://www.moat.com:
from sst.actions import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import requests

# 1.  Verify that the "Try These" links are random and that they work.
def findTryTheseLinks():
  driver = webdriver.Firefox()
  driver.get("http://www.moat.com") #load page
  # checks that it hits the correct url
  assert "Moat" in driver.title
  # finds the a tags located inside the div with id search-suggestions-box
  tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
  # sets the text of the first link to a variable link_a
  link1 = tryTheseLinksList[0].text
  link2 = tryTheseLinksList[1].text
  link3 = tryTheseLinksList[2].text
  driver.close()


# return check1 = findTryTheseLinks()
# return check2 = findTryTheseLinks()
# if check1 == check2
#   true


# link = driver.find_element_by_tag_name('a')
# print link

# 2.  Verify that the "Recently Seen Ads" are no more than half an hour old.

# 3.  Verify that the ad counts are correct, even when they are over 100.

# 4.  Verify the "Share this Ad" feature.
