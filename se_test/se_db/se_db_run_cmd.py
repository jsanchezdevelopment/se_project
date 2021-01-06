#!/usr/bin/python

import os
from os.path import expanduser
from dotenv import load_dotenv
import mysql.connector

def se_db_run_cmd(query,values):
  home = expanduser("~")
  config_path = home + "/.app_config/.env_db"
  load_dotenv(dotenv_path=config_path)

  try:
      mydb = mysql.connector.connect(
      host=os.getenv("MYSQL_HOST"),
      user=os.getenv("MYSQL_USER"),
      password=os.getenv("MYSQL_PASSWORD"),
      database=os.getenv("MYSQL_DATABASE")
      )

      mycursor = mydb.cursor()

      if isinstance(values, tuple):
        mycursor.execute(query, values)
      elif isinstance(values, list):
        mycursor.executemany(query, values)
      else:
        print('Unsupported MySQL Datastructure!')

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
  except mysql.connector.Error as err:
      print("MySQL Error: {}".format(err))

if __name__ == "__main__":
    se_db_run_cmd()
