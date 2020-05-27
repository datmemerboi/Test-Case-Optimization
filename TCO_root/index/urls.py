from django.urls import path
from . import views

urlpatterns = [
	path('', views.loadIndex, name="index")
]