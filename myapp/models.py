from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Movies(models.Model):
	title=models.CharField(max_length=80)
	plot = models.CharField(max_length=500)
	Director=models.CharField(max_length=50)
	writer=models.CharField(max_length=500,default='')
	cast=models.CharField(max_length=5500,default='')
	rating=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)])
	def __str__(self):
		return self.title