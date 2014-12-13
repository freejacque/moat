import unittest
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class MoatSearch(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()


# 3.  Verify that the ad counts are correct, even when they are over 100.
  def test_ad_counts_are_correct(self):
    driver = self.driver
    driver.get("http://www.moat.com")
    searchInput = driver.find_element_by_name("q")
    searchInput.send_keys("pizza hut")
    searchInput.send_keys(Keys.RETURN)
    printedNumOfAds  = driver.find_elements(By.XPATH, "//p[@class='query-summary']")
    siteAdCount = int(printedNumOfAds[0].text.strip(' ads for pizza hut'))
    try:
      element = driver.find_elements(By.XPATH, "//div[@class='more-holder']/button")
    except NoSuchElementException:
      return False
    return True
    while element == True:
      moreAdsButton = driver.find_elements(By.XPATH, "//div[@class='more-holder']/button")
      button = moreAdsButton[0]
      time.sleep(2)
      print "clicking"
      button.click()

      if element == False:
        break
    time.sleep(2)
    ads = driver.find_elements(By.XPATH, "*//div[@class='adcontainer']")
    numberOfAds = int(len(ads))
    print siteAdCount
    print numberOfAds
    self.assertTrue(siteAdCount == numberOfAds)


  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
