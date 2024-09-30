from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    encoding_method = models.CharField(max_length=10, choices=[
        ('base64', 'Base64'),
        ('hash', 'Hash')
    ], default='base64')

    def __str__(self):
        return f"{self.user.username}'s Profile"

class UserInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]