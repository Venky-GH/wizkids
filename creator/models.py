from django.db import models

# Create your models here.
class course (models.Model):
    cid = models.IntegerField()
    coursename = models.TextField(max_length=100)
    desc = models.TextField(max_length=200)
    def __str__(self):
        return self.coursename
    # code = models.CharField(max_length=2)
    # res = models.FileField(upload_to='media/')

class topic (models.Model):
    tid = models.IntegerField()
    cid = models.ForeignKey(course, on_delete=models.CASCADE)
    topicname = models.TextField(max_length=100)
    topicdesc = models.TextField(max_length=200)
    oid = models.IntegerField()
    def __str__(self):
        return self.topicname

class content (models.Model):
    conid = models.IntegerField()
    tid = models.ForeignKey(topic, on_delete=models.CASCADE)
    code = models.CharField(max_length=1)
    data = models.TextField(max_length=300)
    oid = models.IntegerField()
    def __str__(self):
        return self.code
