from django.urls import path
from . import views

urlpatterns = [
	path('', views.resultIndex, name = "result index"),
	path('PSO/', views.psoResult, name = "PSO result"),
	path('GA/', views.gaResult, name = "GA result"),
	path('compare/', views.compareResult, name = "compare results"),
	path('suite/PSO', views.psoSuite, name = "PSO suite"),
	path('suite/GA', views.gaSuite, name = "GA suite")
]