from django.urls import path
from . import views

urlpatterns = [
	path('', views.dataIndexFn, name="index"),
	path('display/', views.dataDisplayFn, name="display"),
	path('csv/', views.dataCSVFn, name="csv"),
	path('tsv/', views.dataTSVFn, name="tsv")
]