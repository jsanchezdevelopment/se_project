#!/usr/bin/python

from datetime import datetime
from se_run_ff import se_run_ff
from se_run_ch import se_run_ch
from se_datastructures import create_data_structure
from se_db.se_db import se_db
import time

def se_main():

  print("=== RUNNING FIREFOX TEST ===")
  ds = create_data_structure()
  # time stamp for test
  ds["test_result"]["TimeStamp"] = datetime.now().strftime("%Y%m%d.%H:%M:%S:%f")
  print("Test Date/Time:",ds["test_result"]["TimeStamp"])
  se_run_ff(ds)
  pf = "None"
  for keys in ds["step_result"]:
    if ds["step_result"][keys]["StepResult"] == "Fail":
      pf = "Fail"
      ds["test_result"]["Result"] = pf
      break
  if pf == "None":
    ds["test_result"]["Result"] = "Pass"
  
  se_db(ds)


  print("=== RUNNING CHROME TEST ===")
  ds = create_data_structure()
  # time stamp for test
  ds["test_result"]["TimeStamp"] = datetime.now().strftime("%Y%m%d.%H:%M:%S:%f")
  print("Test Date/Time:",ds["test_result"]["TimeStamp"])
  se_run_ch(ds)
  pf = "None"
  for keys in ds["step_result"]:
    if ds["step_result"][keys]["StepResult"] == "Fail":
      pf = "Fail"
      ds["test_result"]["Result"] = pf
      break
  if pf == "None":
    ds["test_result"]["Result"] = "Pass"
  
  se_db(ds)

if __name__ == "__main__":
    se_main()
