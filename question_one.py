#!/usr/bin/python

# import selenium
# import sys
# import unittest

# Question 1:
# Please write a small handful of Selenium tests in Python against http://www.moat.com:
from sst.actions import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import requests





# 1.  Verify that the "Try These" links are random and that they work.
def checkLinksRandomnessAndEffect():
  driver = webdriver.Firefox()
  driver.get("http://www.moat.com") #load page
  # checks that it hits the correct url
  assert "Moat" in driver.title
  # finds the a tags located inside the div with id search-suggestions-box
  element = driver.find_element(By.XPATH, "//div[@id='search-suggestions-box']/a")
  # sets the text of the first link to a variable link_a
  link_a = element.text
  print link_a

  driver.close()



# link = driver.find_element_by_tag_name('a')
# print link

# 2.  Verify that the "Recently Seen Ads" are no more than half an hour old.

# 3.  Verify that the ad counts are correct, even when they are over 100.

# 4.  Verify the "Share this Ad" feature.
