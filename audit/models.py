from django.db import models
from django.conf import settings

# Create your models here.
class Audit(models.Model):
    action = models.CharField(max_length=100)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='audits')
    performed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='performed_audits')
    time_stamp = models.DateTimeField(auto_now_add=True)
    meta_json = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.action} by {self.performed_by.name} on {self.time_stamp}"
