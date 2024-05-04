from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from rest_framework import serializers
from project.models import Activity
from django.http import HttpResponse

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'is_read', 'created_at']


class NotificationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        for i in notifications:
            i.is_read = True
            i.save()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)


def every_day(request):
    activity = Activity.objects.filter(project__completed = False)
    for i in activity:
        Notification(user = i.user, title = f'{i.project.name}, message = {i.project.name} {i.project.id} please do not forget to update the data').save()
    return HttpResponse("Task executed successfully", status=200)

def every_week(request):
    activity = Activity.objects.filter(project__completed = False)
    for i in activity:
        i.show_editing = True
        Notification(user = i.user, title = f'{i.project.name}, message = {i.project.name} {i.project.id} sent for verification').save()
    return HttpResponse("Task executed successfully", status=200)