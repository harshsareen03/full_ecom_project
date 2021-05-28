from django.db import models
from django.contrib.auth.models import User


class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    message = models.TextField()
    subject = models.TextField(default='SOME STRING')

    def __str__(self):
        return (self.name)
