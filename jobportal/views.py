from django.shortcuts import render, redirect, get_object_or_404
from .models import job, internship, ApplicationRequest


def jobportal_view(request):
    jobs = job.objects.all().order_by('-date_posted')  # Fetch jobs from the database
    internships = internship.objects.all().order_by('-date_posted')  # Fetch internships from the database
    return render(request, 'jobportal.html', {'jobs': jobs, 'internships': internships})


def apply_view(request, opportunity_type, opportunity_id):
    if opportunity_type == 'job':
        opportunity = get_object_or_404(job, id=opportunity_id)
    elif opportunity_type == 'internship':
        opportunity = get_object_or_404(internship, id=opportunity_id)
    else:
        return redirect('jobportal')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cover_letter = request.POST.get('cover_letter')

        # Save the application to the database
        ApplicationRequest.objects.create(
            opportunity_type=opportunity_type.capitalize(),
            opportunity_id=opportunity_id,
            name=name,
            email=email,
            phone=phone,
            cover_letter=cover_letter
        )

        return redirect('jobportal')

    return render(request, 'apply.html', {
        'opportunity_type': opportunity_type.capitalize(),
        'opportunity_title': opportunity.title,
    })