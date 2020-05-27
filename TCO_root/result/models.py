from django.db import models

class Record():
	TEST_ID: str
	TEST_CASE: str
	PRE_CONDITIONS: str
	PRECEDENCE: str
	COMPLEXITY: str
	PRE_CON_COUNT: int
	WEIGHTAGE: float
	DIFF: float