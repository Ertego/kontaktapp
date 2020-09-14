from uuid import uuid4

from django.db import models

# Create your models here.

class ContactEntry(models.Model):
    name = models.CharField(max_length=25)
    birthday = models.DateField()
    uuid = models.UUIDField(default=uuid4, primary_key=True)
