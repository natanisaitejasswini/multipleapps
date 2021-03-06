from __future__ import unicode_literals
from django.db import models
  # Our Super Basic Model.
class Course(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)