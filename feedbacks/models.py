from django.db import models

# Create your models here.

class feedback(models.Model):
	userid = models.IntegerField()
	summary = models.TextField(max_length=100)



class subscribe(models.Model):
	userid = models.IntegerField()
	#token = models.CharField(max_length=20)
	check = models.BooleanField(default=0)
	date = models.DateTimeField(auto_now_add=True)

class tokens(models.Model):
	token = models.CharField(max_length=20)