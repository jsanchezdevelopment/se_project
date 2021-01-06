#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from se_run_tests import se_run_tests

def se_run_ch(ds):

  # load the driver for the browser
  # Windows Chrome driver
  service = Service('chromedriver')
  service.start()
  browser = webdriver.Remote(service.service_url)
  
  print(browser.capabilities['browserName'])
  print(browser.capabilities['browserVersion'])

  ds["test_result"]["Browser"] = browser.capabilities['browserName']
  ds["test_result"]["BrowserVersion"] = browser.capabilities['browserVersion']

  se_run_tests(browser,ds)

if __name__ == "__main__":
    se_run_ch()
