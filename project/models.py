from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True) 
    document = models.FileField(upload_to='project_documents/', null=True, blank=True)  
    complete = models.BooleanField(default=False)
    tr_document = models.FileField(upload_to='project_translate_documents/', null=True, blank=True)  

    def __str__(self):
        return f"{self.number} - {self.name}"

class Activity(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=255)
    translators = models.ManyToManyField(User, related_name='translation_activities')
    hours_spent = models.FloatField(default=0.0)
    hours_remaining = models.FloatField(default=0.0)
    text_produced = models.FloatField(default=0.0)  
    text_remaining = models.FloatField(default=0.0)  
    managers = models.ManyToManyField(User, related_name='managed_projects')
    chief_editors = models.ManyToManyField(User, related_name='edited_projects')
    show_editing = models.BooleanField(default=False)

    def total_expected_hours(self):
       
        return self.hours_spent + self.hours_remaining

    def total_expected_text(self):
       
        return self.text_produced + self.text_remaining

    def __str__(self):
        return self.name



