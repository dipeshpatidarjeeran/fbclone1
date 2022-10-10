from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here

class Post(models.Model):
	photo=models.ImageField(null=True,blank=True,upload_to='images/')
	author= models.ForeignKey(User,related_name='imageuser', on_delete=models.CASCADE,default='')
	title=models.CharField(max_length=70)
	discription=models.TextField(max_length=10000)
	created_on = models.DateTimeField(auto_now_add=True,blank=True)
	likes=models.ManyToManyField(User,default=None,blank=True,related_name='likes')
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

class Comment(models.Model):
	post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	content=models.TextField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True,blank=True,editable=False)
	def __str__(self):
		return str(self.post)

class Student(models.Model):
	name=models.CharField(max_length=70)
	roll=models.IntegerField()
	city=models.CharField(max_length=70)

# this signal creates auth token for users
# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
# 	if created:
# 		Token.objects.create(user=instance)
