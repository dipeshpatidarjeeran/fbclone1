from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here

class Post(models.Model):
	photo=models.ImageField(null=True,blank=True,upload_to='images/')
	post_user = models.ForeignKey(User,related_name='imageuser', on_delete=models.CASCADE,default='')
	title=models.CharField(max_length=70)
	discription=models.TextField(max_length=140)
	