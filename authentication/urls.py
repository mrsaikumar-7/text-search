# authentication/urls.py
from django.urls import path
from .views import CreateUserView, LoginView, UserDetailsView

# Define URL patterns for authentication and user details
urlpatterns = [
    # URL pattern for user registration
    path('auth/register/', CreateUserView.as_view(), name='register'),

    # URL pattern for user login
    path('auth/login/', LoginView.as_view(), name='login'),

    # URL pattern for retrieving, updating, and deleting user details
    path('auth/user/<int:pk>', UserDetailsView.as_view(), name='user-details'),
]
