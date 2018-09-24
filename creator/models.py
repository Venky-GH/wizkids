from django.db import models

# Create your models here.
class creator (models.Model):
    tid = models.IntegerField()
    code = models.CharField(max_length=2)
    res = models.FileField(upload_to='media/')