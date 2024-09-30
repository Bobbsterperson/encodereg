from django.db import models
from django.contrib.auth.models import User

class UserInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # Return the first 50 characters of the text
