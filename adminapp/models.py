from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Added phone number field
    comments = models.TextField(max_length=150)

    def _str_(self):
        return self.name

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
