from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    grade = models.CharField(
        max_length=2,
        choices=[
            ("A", "A"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B", "B"),
            ("B-", "B-"),
            ("C+", "C+"),
            ("C", "C"),
            ("C-", "C-"),
            ("D", "D"),
            ("F", "F"),
        ],
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def grade_points(self):
        # Mapping letter grades to GPA scale
        grade_map = {
            "A": 4.00,
            "A-": 3.67,
            "B+": 3.33,
            "B": 3.00,
            "B-": 2.67,
            "C+": 2.33,
            "C": 2.00,
            "C-": 1.67,
            "D": 1.00,
            "F": 0.00,
        }
        return grade_map.get(self.grade, 0.00)

    def __str__(self):
        return f"{self.name} - {self.grade} - {self.credit} Credits"
