from __future__ import unicode_literals

from django.db import models


# Create your models here.
class SurveyData(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	phoneno = models.CharField(max_length=12)
	mobileno = models.CharField(max_length=15)
	network = models.CharField(max_length=30)
	television = models.CharField(max_length=30)
	tvchannels = models.CharField(max_length=30)
	newschannels = models.CharField(max_length=30)
	refrigerator = models.CharField(max_length=30)
	twowheelers = models.CharField(max_length=30)
	tractor = models.CharField(max_length=30)
	soap = models.CharField(max_length=30)
	shampoo = models.CharField(max_length=30)
	detergantbar = models.CharField(max_length=30)
	detergantpowder = models.CharField(max_length=30)

	def __str__(self):
		return self.name