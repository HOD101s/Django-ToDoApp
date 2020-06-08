from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.init),
	path('add_todo/', views.add_todo),
	path('completed_todo/<int:pk>', views.completed_todo),
	path('delete_todo/<int:pk>', views.delete_todo),
]
