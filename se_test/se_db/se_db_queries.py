
sqlTestResult = """INSERT INTO test_result (TimeStamp, Browser, BrowserVersion,MetaVersion, Result, URL) VALUES (%s, %s, %s, %s, %s, %s)"""

sqlStepResult = """INSERT INTO step_result 
         (TimeStamp, ParentTimeStamp, ElementID, URL, StepName, StepResult,StepText) 
         VALUES (%s, %s, %s, %s, %s, %s, %s)"""
