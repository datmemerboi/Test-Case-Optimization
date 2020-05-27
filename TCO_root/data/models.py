from django.db import models

class Record():
	TEST_ID:str
	TEST_CASE:str
	PRE_CONDITIONS:str
	TEST_STEPS:str
	PRECEDENCE:str
	TEST_DATA:str
	EXPECTED_RESULT:str
	ACTUAL_RESULT:str
	PASS_FAIL:str
	COMPLEXITY:str
	PRE_CON_COUNT:int
	WEIGHTAGE:float
	DIFF:float