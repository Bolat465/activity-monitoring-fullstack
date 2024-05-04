from django.urls import path
from .views import LoginView, UserLogoutView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
