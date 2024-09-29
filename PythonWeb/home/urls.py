from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('home/', views.index),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login')
]