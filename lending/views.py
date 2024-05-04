from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from project.views import get_projects

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)

        # Retrieve projects for the logged-in user
        user_projects = get_projects(self.request.user)

        # Count completed projects
        completed_projects_count = sum(1 for project in user_projects if project.complete)

        # Update the context with new keys
        context.update({
            'projects': user_projects,
            'pr_count': user_projects.count(),
            'pr_compl': completed_projects_count
        })

        return context
     


