from django.shortcuts import render
# from django.http import HttpResponse
from .models import Record
import json as JSON
import os

def resultIndex(request):
	return render( request, "resultindex.html")

def createRecord(filename):
	pathfile = os.path.join( os.path.dirname(__file__), '..', '..', 'result' , filename)
	File = open(pathfile,'r')
	content = File.read().split("\n")
	File.close()

	data = []
	for ind in range(1, len(content)):
		if len(content[ind].split('\t'))>7:
			record = Record()
	 	
			record.TEST_ID = content[ind].split('\t')[0]
			record.TEST_CASE = content[ind].split('\t')[1]
			record.PRE_CONDITIONS = content[ind].split('\t')[2]
			record.PRECEDENCE = content[ind].split('\t')[3]
			record.COMPLEXITY = content[ind].split('\t')[4]
			record.PRE_CON_COUNT = content[ind].split('\t')[5]
			record.WEIGHTAGE = content[ind].split('\t')[6]
			record.DIFF = content[ind].split('\t')[7]

			data.append(record)
	return data

def psoResult(request):

	path = os.path.join( os.path.dirname(__file__), '..', '..', 'result', 'result.json')
	File = open(path, 'r')
	json = File.read()
	File.close()
	json = JSON.loads(json)

	data = createRecord('PSO Result.tsv')

	return render( request, "pso result.htm.j2", {
		"PSO": json['PSO'], "xaxis": json['PSO']['xaxis'], "yaxis": json['PSO']['yaxis'], "data": data
		})

def gaResult(request):
	path = os.path.join( os.path.dirname(__file__), '..', '..', 'result', 'result.json')
	File = open(path, 'r')
	json = File.read()
	File.close()
	json = JSON.loads(json)

	data = createRecord('GA Result.tsv')

	return render( request, "ga result.htm.j2", {
		"GA": json['GA'], "xaxis": json['GA']['xaxis'], "yaxis": json['GA']['yaxis'], "data": data
		})

def compareResult(request):
	path = os.path.join( os.path.dirname(__file__), '..', '..', 'result', 'result.json')
	File = open(path, 'r')
	json = File.read()
	File.close()
	json = JSON.loads(json)

	return render(request, "compare.htm.j2", {
		"PSO":json['PSO'], "GA":json['GA'], "Equality":json['Equality'], "maximumIterations":json['maximumIterations']
		})
def psoSuite(request):
	data = createRecord('PSO Result.tsv')
	return render(request, "pso suite.htm.j2", {"data": data, "title":"PSO test suite"})

def gaSuite(request):
	data = createRecord('GA Result.tsv')
	return render(request, "ga suite.htm.j2", {"data":data, "title":"GA test suite"})