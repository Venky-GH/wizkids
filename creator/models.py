from django.db import models

# Create your models here.
# class course (models.Model):
#     ids = models.IntegerField()
#     title = models.TextField(max_length=100)
#     desc = models.TextField(max_length=200)
#     def __str__(self):
#         return self.title + ' | ' + str(self.ids)
#     # code = models.CharField(max_length=2)
#     # res = models.FileField(upload_to='media/')
#
# class topic (models.Model):
#     ids = models.IntegerField()
#     cid = models.ForeignKey(course, on_delete=models.CASCADE)
#     title = models.TextField(max_length=100)
#     desc = models.TextField(max_length=200)
#     oid = models.IntegerField()
#     def __str__(self):
#         return self.title
#
# class content (models.Model):
#     conid = models.IntegerField()
#     tid = models.ForeignKey(topic, on_delete=models.CASCADE)
#     code = models.CharField(max_length=1)
#     data = models.TextField(max_length=300)
#     oid = models.IntegerField()
#     def __str__(self):
#         return self.code
