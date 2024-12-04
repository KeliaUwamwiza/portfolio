from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonalInfo
from .forms import PersonalInfoForm

def portfolio_view(request):
    # Fetch the first portfolio entry
    info = PersonalInfo.objects.first()
    
    # Split the skills field into a list if info exists
    skills_list = info.skills.split(',') if info else []
    
    return render(request, 'portfolio/index.html', {'info': info, 'skills_list': skills_list})

def update_portfolio(request):
    # Get the first (or only) portfolio entry or create one if it doesn't exist
    info, created = PersonalInfo.objects.get_or_create(pk=1)
    
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return redirect('portfolio')  # Redirect to the portfolio page after saving
    else:
        form = PersonalInfoForm(instance=info)
    
    return render(request, 'portfolio/update.html', {'form': form})

# portfolio/views.py
def delete_portfolio(request):
    info = get_object_or_404(PersonalInfo, pk=1)  # Assuming only one entry
    info.delete()
    return redirect('portfolio')  # Redirect to the portfolio page
