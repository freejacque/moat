# Question 1:
# Please write a small handful of Selenium tests in Python against http://www.moat.com:


import unittest
import random
from sst.actions import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import Select

class MoatSearch(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()

  # def test_for_correct_page(self):
  #   driver = self.driver
  #   driver.get("http://www.moat.com") #load page
  #   self.assertIn("Moat", driver.title)

  # 1.  Verify that the "Try These" links are random
  # def test_try_these_link_randomness(self):
  #   driver = self.driver
  #   driver.get("http://www.moat.com") #load page
  #   tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
  #   links1 = []
  #   links1.append(tryTheseLinksList[0].text)
  #   links1.append(tryTheseLinksList[1].text)
  #   links1.append(tryTheseLinksList[2].text)
  #   driver.refresh()
  #   tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
  #   links2 = []
  #   links2.append(tryTheseLinksList[0].text)
  #   links2.append(tryTheseLinksList[1].text)
  #   links2.append(tryTheseLinksList[2].text)
  #   self.assertTrue(links1 != links2)

  # and that they work.
  # def test_try_these_links_work(self):
  #   driver = self.driver
  #   driver.get("http://www.moat.com")
  #   tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
  #   randomLink = random.choice(tryTheseLinksList)
  #   linkText = randomLink.text.strip('u').lower()
  #   print linkText
  #   randomLink.click()
  #   querySummary = driver.find_elements(By.XPATH, "//p[@class='query-summary']/a")
  #   queryText = querySummary[0].text
  #   print queryText
  #   self.assertTrue(linkText == queryText)

  # 2.  Verify that the "Recently Seen Ads" are no more than half an hour old.
  def test_recently_seen_ads_less_than_half_hour_old(self):
    driver = self.driver
    driver.get("http://www.moat.com")
    recentlySeenAdsList = driver.find_elements(By.XPATH, "*//div[@id='search-sub']/ul/div/li[@class='featured-agencies']/div[@class='hpads']/h2")
    print recentlySeenAdsList
    # for ad in recentlySeenAdsList:
    #   print ad


  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
