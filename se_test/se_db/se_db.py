#!/usr/bin/python

from pprint import pprint
from se_db.se_db_queries import *
from se_db.se_db_run_cmd import se_db_run_cmd

def se_db(ds):

  # prepare the test_result data for the database
  vResult = []
  vResult.append( (ds["test_result"]["TimeStamp"],
  ds["test_result"]["Browser"],
  ds["test_result"]["BrowserVersion"],
  ds["test_result"]["MetaVersion"],
  ds["test_result"]["Result"],
  ds["test_result"]["URL"]) )

  # log the results to the test_result database
  se_db_run_cmd(sqlTestResult,vResult[0])

  # prepare the step_result data for the database
  vResult = []
  for key1 in ds["step_result"]:
    vResult.append( (key1,
    ds["step_result"][key1]["ParentTimeStamp"],
    ds["step_result"][key1]["ElementID"],
    ds["step_result"][key1]["URL"],
    ds["step_result"][key1]["StepName"],
    ds["step_result"][key1]["StepResult"],
    ds["step_result"][key1]["StepText"]) )
  
  # log the results to the step_result database
  se_db_run_cmd(sqlStepResult,vResult)



if __name__ == "__main__":
    se_db()
