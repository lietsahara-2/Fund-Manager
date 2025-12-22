from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, default='user')