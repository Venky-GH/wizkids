from django.db import models

# Create your models here.

class feedback(models.Model):
	userid = models.IntegerField()
	summary = models.TextField(max_length=100)