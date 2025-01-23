from django.db import models

class job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)


class internship(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)



class ApplicationRequest(models.Model):
    OPPORTUNITY_TYPES = [
        ('Job', 'Job'),
        ('Internship', 'Internship'),
    ]

    opportunity_type = models.CharField(max_length=20, choices=OPPORTUNITY_TYPES)
    opportunity_id = models.PositiveIntegerField()  # ID of the job or internship
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    cover_letter = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)


