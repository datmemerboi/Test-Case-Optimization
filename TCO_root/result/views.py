from django.shortcuts import render
import json as JSON
import os

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'result'))

def resultIndex(request):
	return render( request, "resultindex.html")

def extractDataFromFile(fileName):
	with open(os.path.join(BASE_PATH, fileName), 'r') as file:
		content = file.read().split('\n')

	data = []
	for ind in range(1, len(content)):
		if len(content[ind].split('\t')) > 7:
			record = dict(
				TEST_ID = content[ind].split('\t')[0],
				TEST_CASE = content[ind].split('\t')[1],
				PRE_CONDITIONS = content[ind].split('\t')[2],
				PRECEDENCE = content[ind].split('\t')[3],
				COMPLEXITY = content[ind].split('\t')[4],
				PRE_CON_COUNT = content[ind].split('\t')[5],
				WEIGHTAGE = content[ind].split('\t')[6],
				DIFF = content[ind].split('\t')[7]
			)
			data.append(record)
	return data

def psoResult(request):
	with open(os.path.join(BASE_PATH, 'result.json'), 'r') as file:
		jsonContent = JSON.load(file)

	data = extractDataFromFile('PSO Result.tsv')
	responseObj = {
		"PSO": jsonContent['PSO'],
		"x_axis": jsonContent['PSO']['x_axis'],
		"y_axis": jsonContent['PSO']['y_axis'],
		"data": data
	}
	return render(request, "pso result.htm.j2", JSON.loads(JSON.dumps(responseObj)))

def gaResult(request):
	with open(os.path.join(BASE_PATH, 'result.json'), 'r') as file:
		jsonContent = JSON.load(file)

	data = extractDataFromFile('GA Result.tsv')
	responseObj = {
		"GA": jsonContent['GA'],
		"x_axis": jsonContent['GA']['x_axis'],
		"y_axis": jsonContent['GA']['y_axis'],
		"data": data
	}
	return render(request, "ga result.htm.j2", JSON.loads(JSON.dumps(responseObj)))

def compareResult(request):
	with open(os.path.join(BASE_PATH, 'result.json'), 'r') as file:
		jsonContent = JSON.load(file)
	return render(request, "compare.htm.j2", jsonContent)

def psoSuite(request):
	data = extractDataFromFile('PSO Result.tsv')
	return render(request, "pso suite.htm.j2", { "data": data, "title": "PSO test suite" })

def gaSuite(request):
	data = extractDataFromFile('GA Result.tsv')
	return render(request, "ga suite.htm.j2", { "data": data, "title": "GA test suite" })