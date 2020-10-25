from django.shortcuts import render

def loadIndex(request):
	return render(request, 'index.html')