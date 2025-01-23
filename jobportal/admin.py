from django.contrib import admin
from .models import job, internship, ApplicationRequest

admin.site.register(job)
admin.site.register(internship)
admin.site.register(ApplicationRequest)