from django.db import models

# Create your models here

class Post(models.Model):
	photo=models.ImageField(null=True,blank=True,upload_to='images/')
	title=models.CharField(max_length=70,default='')
	discription=models.TextField(max_length=140,default='')