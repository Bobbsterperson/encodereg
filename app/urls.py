from django.urls import path
from .views import register, input_text, user_login

urlpatterns = [
    path('', register, name='register'),
    path('input-text/', input_text, name='input_text'),
    path('login/', user_login, name='login'),
]
