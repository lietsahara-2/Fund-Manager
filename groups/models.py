from django.db import models
from django.conf import settings

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    currency =  models.CharField(max_length=10, default='KSH')
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="admin_groups")

    def __str__(self):
        return self.name
    
class Memberships(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="memberships")
    joined_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    contribution_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.name} in {self.group.name}"


