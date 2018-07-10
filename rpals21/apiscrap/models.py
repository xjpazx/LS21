from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Robot(models.Model):
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('ON_GOING', 'On Going'),
        ('ERROR', 'Error'),
        ('FINISHED', 'Finished')
    )

    started = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField(null=True, blank=True)
    input_data = models.TextField()
    output_data = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='CREATED')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='robots')
