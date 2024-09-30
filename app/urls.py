from django.urls import path
from .views import register, input_text

urlpatterns = [
    path('', register, name='register'),
    path('input-text/', input_text, name='input_text'),  # Add this line
]
