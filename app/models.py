from django.db import models

# Create your models here.

class MyDo(models.Model):
	activity = models.CharField(max_length=1000)
	status = models.BooleanField(default=False)
	starttimestamp = models.DateTimeField()
	endtimestamp = models.DateTimeField()

	def __str__(self):
		return self.activity
