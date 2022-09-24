from django.db import models

# Create your models here.
class Books(models.Model):
	bname = models.CharField(max_length=80)
	bprice = models.IntegerField()
	bauthor = models.CharField(max_length=120)
	bdesc = models.CharField(max_length=200)

