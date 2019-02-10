from django.db import models
from django.utils import timezone
import datetime


class Save (models.Model):
	user = models.CharField(max_length = 100)
	cipher_text = models.CharField(max_length = 1000)
	algoritm = models.IntegerField(default=0)
	date = models.DateTimeField('date creation')
	firm = models.CharField(max_length = 10000, default='')


datetime.timedelta(days=1)

# Create your models here.
