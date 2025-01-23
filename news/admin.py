from django.contrib import admin
from .models import news, announcement

admin.site.register(news)
admin.site.register(announcement)