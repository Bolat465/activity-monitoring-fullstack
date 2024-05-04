from django.shortcuts import render,redirect
from .models import Project, Activity

def get_projects(user):
    projects = Project.objects.filter(activities__translators=user).distinct() 
    return projects


def update_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.method == 'POST':
        activity.hours_spent = float(request.POST.get('hours_spent', 0.0))
        activity.hours_remaining = float(request.POST.get('hours_remaining', 0.0))
        activity.text_produced = float(request.POST.get('text_produced', 0.0))
        activity.text_remaining = float(request.POST.get('text_remaining', 0.0))
        activity.save()
        if(activity.text_produced >= 100):
            activity.project.complete = True
            activity.project.save()
        
        return redirect(request.META.get('HTTP_REFERER', 'default_fallback_url'))
    


def check_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.method == 'POST':
        activity.show_editing = False
        activity.save()

        return redirect(request.META.get('HTTP_REFERER', 'default_fallback_url'))
    
