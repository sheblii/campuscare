from django import forms

from .models import Subject


class SubjectForm(forms.ModelForm):
    CREDIT_CHOICES = [(1, "1 Credit"), (2, "2 Credits"), (3, "3 Credits")]
    GRADE_CHOICES = [
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
    ]

    credit = forms.ChoiceField(
        choices=CREDIT_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    grade = forms.ChoiceField(
        choices=GRADE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Subject
        fields = ["name", "credit", "grade"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
