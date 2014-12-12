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

  def test_for_correct_page(self):
    driver = self.driver
    driver.get("http://www.moat.com") #load page
    self.assertIn("Moat", driver.title)

  def test_try_these_link_randomness(self):
    driver = self.driver
    driver.get("http://www.moat.com") #load page
    tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
    links1 = []
    links1.append(tryTheseLinksList[0].text)
    links1.append(tryTheseLinksList[1].text)
    links1.append(tryTheseLinksList[2].text)
    driver.refresh()
    tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
    links2 = []
    links2.append(tryTheseLinksList[0].text)
    links2.append(tryTheseLinksList[1].text)
    links2.append(tryTheseLinksList[2].text)
    self.assertTrue(links1 != links2)


  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
