from django.urls import path
from .views import NotificationsAPIView, every_day, every_week


urlpatterns = [
    path('', NotificationsAPIView.as_view(), name='api_notifications'),
    path('every_day/',every_day,name = 'every_day'),
    path('every_week/',every_week,name = 'every_week'),
]
