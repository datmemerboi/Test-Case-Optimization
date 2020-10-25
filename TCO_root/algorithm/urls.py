from django.urls import path
from . import views

urlpatterns = [
	path('', views.algoIndex, name = "algorithm index"),
	path('PSO/', views.algoPSO, name = "pso algorithm"),
	path('GA/', views.algoGA, name = "ga algorithm")
]