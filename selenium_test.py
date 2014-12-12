# Question 1:
# Please write a small handful of Selenium tests in Python against http://www.moat.com:


import unittest
from sst.actions import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import Select

class MoatSearch(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()

  def test_try_these_link_randomness(self):
    driver = self.driver
    driver.get("http://www.moat.com") #load page
    self.assertIn("Moat", driver.title)
    tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
    link1 = tryTheseLinksList[0].text
    link2 = tryTheseLinksList[1].text
    link3 = tryTheseLinksList[2].text
    driver.refresh()
    tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
    link4 = tryTheseLinksList[0].text
    link5 = tryTheseLinksList[1].text
    link6 = tryTheseLinksList[2].text


  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
