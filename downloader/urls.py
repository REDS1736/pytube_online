from django.urls import path
from downloader import views

urlpatterns = [
	path('', views.index, name='index')
]
