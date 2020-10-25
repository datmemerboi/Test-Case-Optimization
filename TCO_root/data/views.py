import os
from django.shortcuts import render
from django.http import HttpResponse

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'dataset'))

def dataIndexFn(request):
	return render(request, 'dataindex.html')

def dataDisplayFn(request):
	with open(os.path.join(BASE_PATH, "Test Case Dataset.tsv"), 'r') as File:
		content = File.read().split("\n")

	data = []
	for ind in range(1, len(content)):
		record = dict(
			TEST_ID = content[ind].split('\t')[0],
			TEST_CASE = content[ind].split('\t')[1],
			PRE_CONDITIONS = content[ind].split('\t')[2],
			TEST_STEPS = content[ind].split('\t')[3],
			PRECEDENCE = content[ind].split('\t')[4],
			COMPLEXITY = content[ind].split('\t')[5],
			TEST_DATA = content[ind].split('\t')[6],
			EXPECTED_RESULT = content[ind].split('\t')[7],
			ACTUAL_RESULT = content[ind].split('\t')[8],
			PASS_FAIL = content[ind].split('\t')[9]
		)
		data.append(record)

	return render(request, "display.htm.j2", { 'data': data })

def dataCsvFn(request):
	File = open(os.path.join(BASE_PATH, "Test Case Dataset.csv"), 'rb').read()
	response =  HttpResponse(File, content_type = 'text/csv')
	response['Content-Disposition'] = 'attachment; filename="Dataset of TCO.csv"'
	return response

def dataTsvFn(request):
	File = open(os.path.join(BASE_PATH, "Test Case Dataset.tsv"), 'rb').read()
	response =  HttpResponse(File, content_type = 'text/tsv')
	response['Content-Disposition'] = 'attachment; filename="Dataset of TCO.tsv"'
	return response