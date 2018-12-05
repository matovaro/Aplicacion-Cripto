from django.db import models
from django.utils import timezone
import datetime


class Save (models.Model):
	text_plain = models.CharField(max_length = 1000)
	cipher_text = models.CharField(max_length = 1000)
	algoritm = models.IntegerField(default=0)
	date = models.DateTimeField('date creation')

	def __str__(self):
		return self.text_plain

datetime.timedelta(days=1)

# Create your models here.
