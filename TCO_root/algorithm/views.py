from django.shortcuts import render
import os

def algoIndex(request):
	return render(request, 'algorithm.html')

def algoPSO(request):
	path = os.path.join( os.path.dirname(__file__), '..', '..', 'algo', 'PSO.py')
	File = open( path, 'r')
	pso_content = File.read()
	pso_content = pso_content[297:1857].split('\n')
	File.close()

	return render(request, 'pso algo.htm.j2', {'pso_content':pso_content});

def algoGA(request):
	path = os.path.join( os.path.dirname(__file__), '..', '..', 'algo', 'GA.py')
	File = open( path, 'r')
	ga_content = File.read()
	ga_content = ga_content[169:961].split('\n')
	File.close()

	return render(request, 'ga algo.htm.j2', {'ga_content':ga_content});
