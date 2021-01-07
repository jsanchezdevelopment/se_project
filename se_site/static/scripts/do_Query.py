#!/usr/bin/python

import os
from os.path import expanduser
from dotenv import load_dotenv
import mysql.connector

DEBUG = True

def do_Query(query):
  
  home = expanduser("~")
  config_path = home + "/.app_config/.env_sedb"
  load_dotenv(dotenv_path=config_path)

  if DEBUG:
    print(config_path)
  
  if DEBUG:
    print('Host: ' + os.getenv("MYSQL_HOST"))
    print('User: ' + os.getenv("MYSQL_USER"))
    print('Pwd: ' + os.getenv("MYSQL_PASSWORD"))
    print('Database: ' + os.getenv("MYSQL_DATABASE"))

  cnx = mysql.connector.connect( user=os.getenv("MYSQL_USER"), 
                                 password=os.getenv("MYSQL_PASSWORD"),
                                 host=os.getenv("MYSQL_HOST"),
                                 database=os.getenv("MYSQL_DATABASE")
                               )
  cursor = cnx.cursor()
  cursor.execute(query)
  data = list(cursor.fetchall())
  res = [list(ele) for ele in data]
  if DEBUG:
    for row in res:
      print(row)
    
  cursor.close()
  cnx.close()
  
  return res
