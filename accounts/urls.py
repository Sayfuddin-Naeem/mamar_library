from django.urls import path
from .views import (
    UserRegistrationView, 
    UserLoginView, 
    UserLogoutView, 
    UserAccountUpdateView,
    UserPassChangeView,
    ProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', UserAccountUpdateView.as_view(), name='update_profile'),
    path('profile/update/change_password/', UserPassChangeView.as_view(), name='change_password'),
]
