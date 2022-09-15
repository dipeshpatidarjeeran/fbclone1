from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here

class Post(models.Model):
	photo=models.ImageField(null=True,blank=True,upload_to='images/')
	author= models.ForeignKey(User,related_name='imageuser', on_delete=models.CASCADE,default='')
	title=models.CharField(max_length=70)
	discription=models.TextField(max_length=140)
	created_on = models.DateTimeField(auto_now_add=True,blank=True)
	liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')
	class Meta:
		 ordering = ('-created_on',)

	def __str__(self):
		return str(self.author)
	def num_liked(self):
		return self.liked.count() 

LIKE_CHOICES=(('Like','Like'),('Unlike','Unlike'))

class Like(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(Post,on_delete=models.CASCADE)
	value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=70)

	def __str__(self):
		return str(self.post)