#!/usr/bin/python

from do_Query import do_Query
#from mysql_queries import q_continent_country_count, q_continent_pop

DEBUG = False

def home_get_data(sr):
  #print(sr)
  header = []
  data1 = do_Query("SELECT CAST(TimeStamp AS CHAR),Browser,BrowserVersion,MetaVersion,Result,URL FROM test_result t;")
  data2 = []
  if sr != "StepResult":
    data2 = do_Query("""SELECT CAST(TimeStamp AS CHAR), CAST(ParentTimeStamp AS CHAR), ElementID, URL, StepName, StepResult, StepText FROM step_result where ParentTimeStamp like \"""" + sr + """\";""")
  if DEBUG:
    print()
  
  for row in data1:
    if row[0] == sr:
      print(row)
      header = row

  return data1,data2,header

if __name__ == "__main__":
    home_get_data()
