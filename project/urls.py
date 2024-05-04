from django.urls import path
from .edit import project_detail, save_translated_document
from .views import update_activity, check_activity

urlpatterns = [
    path('<int:project_id>/', project_detail, name='project_detail'),
    path('save_translated_document/<int:project_id>/', save_translated_document, name='save_translated_document'),
    path('activity/update/<int:activity_id>/', update_activity, name='update_activity'),
    path('activity/check/<int:activity_id>/', check_activity, name='check_activity'),

]
