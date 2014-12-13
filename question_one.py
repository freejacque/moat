# Question 1:
# Please write a small handful of Selenium tests in Python against http://www.moat.com:

import unittest
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class MoatSearch(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()

  def test_for_correct_page(self):
    driver = self.driver
    driver.get("http://www.moat.com") #load page
    self.assertIn("Moat", driver.title)

  # 1.  Verify that the "Try These" links are random
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

  # and that they work.
  def test_try_these_links_work(self):
    driver = self.driver
    driver.get("http://www.moat.com")
    tryTheseLinksList = driver.find_elements(By.XPATH, "*//div[@id='search-suggestions-box']/a")
    randomLink = random.choice(tryTheseLinksList)
    linkText = randomLink.text.strip('u').lower()
    randomLink.click()
    querySummary = driver.find_elements(By.XPATH, "//p[@class='query-summary']/a")
    queryText = querySummary[0].text
    self.assertTrue(linkText == queryText)

  # 2.  Verify that the "Recently Seen Ads" are no more than half an hour old.
  def test_recently_seen_ads_less_than_half_hour_old(self):
    driver = self.driver
    driver.get("http://www.moat.com")
    recentlySeenAdsList = driver.find_elements(By.XPATH, "*//li[@class='featured-agencies']/h2")
    for ad in recentlySeenAdsList:
      ageOfAd = int(ad.text.strip(' minutes ago'))
      self.assertTrue(ageOfAd <= 30)

  # 3.  Verify that the ad counts are correct, even when they are over 100.
  def test_ad_counts_are_correct(self):
    driver = self.driver
    driver.get("http://www.moat.com")
    searchInput = driver.find_element_by_name("q")
    searchInput.send_keys("pizza hut")
    searchInput.send_keys(Keys.RETURN)
    printedNumOfAds  = driver.find_elements(By.XPATH, "//p[@class='query-summary']")
    siteAdCount = int(printedNumOfAds[0].text.strip(' ads for pizza hut'))
    i = 0
    while i < 3:
      time.sleep(2)
      moreAdsButton = driver.find_elements(By.XPATH, "//div[@class='more-holder']/button")
      moreAdsButton[0].click()
      i += 1

      if i == 3:
        break
    time.sleep(2)
    ads = driver.find_elements(By.XPATH, "*//div[@class='ad  ']")
    numberOfAds = int(len(ads) + 1)
    print siteAdCount
    print numberOfAds
    self.assertTrue(siteAdCount == numberOfAds)

  # 4.  Verify the "Share this Ad" feature.
  def test_verify_share_this_ad_feature(self):
    driver = self.driver
    driver.get("http://www.moat.com")
    searchInput = driver.find_element_by_name("q")
    searchInput.send_keys("pizza hut")
    searchInput.send_keys(Keys.RETURN)
    ads = driver.find_elements(By.XPATH, "*//div[@class='ad  ']")
    ad = ads[0]
    Hover = ActionChains(driver).move_to_element(ad)
    Hover.perform()
    shareThisAd = driver.find_elements(By.XPATH, "//div[@class='link5']/a")
    shareThisAdText = shareThisAd[0].get_attribute('text')
    self.assertEqual("Share this ad", shareThisAdText)


  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
