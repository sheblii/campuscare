from django.shortcuts import render, redirect, get_object_or_404
from .models import news, announcement

def news_view(request):
    news_list = news.objects.all().order_by('-date_posted')  # Fetch news from the database
    announcements = announcement.objects.all().order_by('-date_posted')  # Fetch announcements from the database
    return render(request, 'news.html', {'news': news_list, 'announcements': announcements})

