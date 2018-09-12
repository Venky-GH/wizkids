from django.db import models

# Create your models here.

class account(models.Model):
	username = models.CharField(max_length=100)
	parentname = models.CharField(max_length=100)
	childname = models.CharField(max_length=100)
	userid = models.IntegerField()
	email = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/', default='images/Screenshot_9.png')