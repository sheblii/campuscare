from django.contrib import admin
from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.news_view, name='news'),                # News view
]
