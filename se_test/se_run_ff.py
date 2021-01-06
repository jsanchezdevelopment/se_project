#!/usr/bin/python

from selenium import webdriver
from se_run_tests import se_run_tests

def se_run_ff(ds):

  # load the driver for the browser
  # Windows Firefox driver
  browser = webdriver.Firefox()
  
  print(browser.capabilities['browserName'])
  print(browser.capabilities['browserVersion'])

  ds["test_result"]["Browser"] = browser.capabilities['browserName']
  ds["test_result"]["BrowserVersion"] = browser.capabilities['browserVersion']

  se_run_tests(browser,ds)

if __name__ == "__main__":
    se_run_ff()
