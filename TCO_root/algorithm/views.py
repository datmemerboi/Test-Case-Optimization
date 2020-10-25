import os
from django.shortcuts import render

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'algo'))

def algoIndex(request):
	return render(request, 'algorithm.html')

def algoPSO(request):
	with open(os.path.join(BASE_PATH, 'PSO.py'), 'r') as file:
		psoAsText = file.read()
	psoAsText = psoAsText[297:1857].split('\n')
	return render(request, 'pso algo.htm.j2', { 'pso_content': psoAsText });

def algoGA(request):
	with open(os.path.join(BASE_PATH, 'GA.py'), 'r') as file:
		gaAsText = file.read()
	gaAsText = gaAsText[169:961].split('\n')
	return render(request, 'ga algo.htm.j2', { 'ga_content': gaAsText });