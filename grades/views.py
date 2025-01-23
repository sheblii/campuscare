from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SubjectForm
from .models import Subject


@login_required
def calculate(request):
    # Handle Delete Action
    if request.method == "POST" and "delete_subject" in request.POST:
        subject_id = request.POST.get("subject_id")
        subject = get_object_or_404(Subject, id=subject_id, user=request.user)
        subject.delete()
        return redirect("calculate")

    # Handle Edit Action
    if request.method == "POST" and "edit_subject" in request.POST:
        subject_id = request.POST.get("subject_id")
        subject = get_object_or_404(Subject, id=subject_id, user=request.user)
        form = SubjectForm(instance=subject)
        return render(
            request, "grades/edit_subject.html", {"form": form, "subject": subject}
        )

    # Handle Save/Edit Changes
    if request.method == "POST" and "save_subject" in request.POST:
        subject_id = request.POST.get("subject_id")
        subject = get_object_or_404(Subject, id=subject_id, user=request.user)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect("calculate")

    # Handle Add Subject
    form = SubjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        subject = form.save(commit=False)
        subject.user = request.user
        subject.save()
        return redirect("calculate")

    # Calculate GPA and Total Credits
    subjects = Subject.objects.filter(user=request.user)
    total_credits = sum(subject.credit for subject in subjects)
    total_grade_points = sum(
        Decimal(subject.credit) * Decimal(subject.grade_points())
        for subject in subjects
    )
    gpa = total_grade_points / total_credits if total_credits > 0 else Decimal("0.00")

    return render(
        request,
        "grades/calculate.html",
        {
            "form": form,
            "subjects": subjects,
            "gpa": round(gpa, 2),
            "total_credits": total_credits,  # Pass total credits to the template
        },
    )
