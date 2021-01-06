#!/usr/bin/python

from datetime import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from se_common import *

def se_run_tests(browser,ds):

  main_ts = ds["test_result"]["TimeStamp"]

  # ===== TEST =====
  # open the browser and web site to test
  delay = 10 # seconds
  url = 'http://classicjs.com/'
  id = 'navbarNav'
  try:
    browser.get(url)
    elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, id)))
    print("Page is ready!")
    r = "Pass"
    t = "Page Loaded"
  except Exception as e:
    msg = "Loading took too much time!"
    handle_error(msg,e)
    r = "Fail"
    t = e.args[0]
  finally: 
    ds["step_result"].update( { datetime.now().strftime("%Y%m%d.%H:%M:%S:%f"): {"ParentTimeStamp": main_ts,"URL": url,"StepText": t,"StepResult":r,"ElementID": id,"StepName": "OpenSite"} })
    if r == "Fail":
      browser.close()
      return

  # able to load site, record the URL
  print('Site: ' + browser.current_url)
  ds["test_result"]["URL"] = browser.current_url

  # get the version
  metaversion = browser.find_element_by_xpath("//meta[@name='version']")
  print('Site Version: ' + metaversion.get_attribute("content"))
  ds["test_result"]["MetaVersion"] = metaversion.get_attribute("content")
  
  browser.set_window_size(1200, 800)

  # ===== TEST =====
  # click on the contact button
  id = "main-contact"
  try:
    element = browser.find_element_by_id(id)
    element.click()
    time.sleep(1)
    print(browser.current_url)
    r = "Pass"
    t = "Found Element"
  except Exception as e:
    handle_error("Click Error",e)
    r = "Fail"
    t = e.args[0]
  finally: 
    ds["step_result"].update( { datetime.now().strftime("%Y%m%d.%H:%M:%S:%f"): {"ParentTimeStamp": main_ts,"URL": browser.current_url,"StepText": t,"StepResult":r,"ElementID": id,"StepName": "GoToContactPage"} })
    if r == "Fail":
      browser.close()
      return
    
  # ===== TEST =====
  # find text
  text = '512-771-4237'
  try:
    find_text(browser,text)
    r = "Pass"
    t = "Found Text: " + text
  except Exception as e:
    handle_error("Find Text Error",e)  
    r = "Fail"
    t = e.args[0]
  finally:
    ds["step_result"].update( { datetime.now().strftime("%Y%m%d.%H:%M:%S:%f"): {"ParentTimeStamp": main_ts,"URL": browser.current_url,"StepText": t,"StepResult":r,"ElementID": "none","StepName": "FindText"} })
    if r == "Fail":
      browser.close()
      return

  # ===== TEST =====
  # click on the resume button
  id = "main-resume"
  try:
    element = browser.find_element_by_id(id)
    element.click()
    time.sleep(1)
    print(browser.current_url)
    r = "Pass"
    t = "Found Element"
  except Exception as e:
    handle_error("Click Error",e)  
    r = "Fail"
    t = e.args[0]
  finally:
    ds["step_result"].update( { datetime.now().strftime("%Y%m%d.%H:%M:%S:%f"): {"ParentTimeStamp": main_ts,"URL": browser.current_url,"StepText": t,"StepResult":r,"ElementID": id,"StepName": "GoToResumePage"} })
    if r == "Fail":
      browser.close()
      return

  # ===== TEST =====
  # find text
  text = 'four years experience developing'
  try:
    find_text(browser,text)
    r = "Pass"
    t = "Found Text: " + text
  except Exception as e:
    handle_error("Find Text Error",e)  
    r = "Fail"
    t = e.args[0]
  finally:
    ds["step_result"].update( { datetime.now().strftime("%Y%m%d.%H:%M:%S:%f"): {"ParentTimeStamp": main_ts,"URL": browser.current_url,"StepText": t,"StepResult":r,"ElementID": "none","StepName": "FindText"} })
    if r == "Fail":
      browser.close()
      return

  # ===== TEST =====
  # find text
  text = 'Thailand is great!'
  try:
    find_text(browser,text)
    r = "Pass"
    t = "Found Text: " + text
  except Exception as e:
    handle_error("Find Text Error",e)  
    r = "Fail"
    t = e.args[0]
  finally:
    ds["step_result"].update( { datetime.now().strftime("%Y%m%d.%H:%M:%S:%f"): {"ParentTimeStamp": main_ts,"URL": browser.current_url,"StepText": t,"StepResult":r,"ElementID": "none","StepName": "FindText"} })
    if r == "Fail":
      browser.close()
      return
 
  # close the browser
  browser.close()


if __name__ == "__main__":
    se_run_tests()
