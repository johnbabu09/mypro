from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Student(models.Model):
	student_name=models.CharField(max_length=30)
	student_id=models.IntegerField()
	student_number=models.IntegerField()
	student_email=models.CharField(max_length=30)
	student_time=models.DateTimeField()

	def __unicode__(self):
		return unicode(self.student_name)
