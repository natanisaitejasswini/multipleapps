from __future__ import unicode_literals
from django.db import models
from ..courseapp.models import Course
from ..loginregapp.models import Userlog
class User_Add(models.Model):
	user = models.ForeignKey(Userlog, related_name='users')
	course = models.ForeignKey(Course, related_name='courses')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True)

