from django.urls import path
from .views import user_profile

app_name = 'profiles'

urlpatterns = [
    path('', user_profile, name='user_profile')
]