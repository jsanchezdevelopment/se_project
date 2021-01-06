#!/usr/bin/python

from se_exceptions import *

def find_text(browser, text):
  if (text in browser.page_source):
    print("Found: " + text) # text exists in page
    return 0
  else:
    #print("Not Found: " + text)
    raise FindTextError("Could not find: " + text)
    return 1

def handle_error(user_msg,e):
  print("===== ERROR =====")
  print(user_msg)
  print(type(e))    # the exception instance
  print(e.args)     # arguments stored in .args
