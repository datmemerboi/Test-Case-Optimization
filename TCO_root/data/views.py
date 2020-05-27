from django.shortcuts import render
from django.http import HttpResponse
from .models import Record
import os
path = os.path.join( os.path.dirname(__file__), '..', '..', 'dataset/')

def dataIndexFn(request):
	return render( request, 'dataindex.html')

def dataDisplayFn(request):
	File = open( path+"Test Case Dataset.tsv", 'r')
	content = File.read().split("\n")
	File.close()

	data = []
	for ind in range(1, len(content)):
		record = Record()
 	
		record.TEST_ID = content[ind].split('\t')[0]
		record.TEST_CASE = content[ind].split('\t')[1]
		record.PRE_CONDITIONS = content[ind].split('\t')[2]
		record.TEST_STEPS = content[ind].split('\t')[3]
		record.PRECEDENCE = content[ind].split('\t')[4]
		record.COMPLEXITY = content[ind].split('\t')[5]
		record.TEST_DATA = content[ind].split('\t')[6]
		record.EXPECTED_RESULT = content[ind].split('\t')[7]
		record.ACTUAL_RESULT = content[ind].split('\t')[8]
		record.PASS_FAIL = content[ind].split('\t')[9]

		data.append(record)

	return render( request, "display.htm.j2", {'data': data})

def dataCSVFn(request):
	if request.method == 'GET':
		File = open( path+"Test Case Dataset.csv", 'rb').read()
		response =  HttpResponse(File, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="Dataset of TCO.csv"'
		return response

def dataTSVFn(request):
	if request.method == 'GET':
		File = open( path+"Test Case Dataset.tsv", 'rb').read()
		response =  HttpResponse(File, content_type='text/tsv')
		response['Content-Disposition'] = 'attachment; filename="Dataset of TCO.tsv"'
		return response