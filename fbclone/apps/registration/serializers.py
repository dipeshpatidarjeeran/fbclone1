from rest_framework import serializers
from .models import Student,Post
from django.contrib.auth.models import User

# class StudentSerializer(serializers.ModelSerializer):
# 	# def validate_roll(self,value):
# 	# 	if value not in Student.objects.get('roll'):
# 	# 		raise serializers.ValidationError('not valid rollno')
# 	# 	return value
# 	class Meta:
# 		model=Student
# 		fields=['id','name','roll','city']

class PostSerializer(serializers.ModelSerializer):
	#author=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='authorpost')
	# author=serializers.PrimaryKeyRelatedField(many=True,read_only=True,)
	class Meta:
		model=Post
		fields=['id','photo','title','discription']	

class UserSerializer(serializers.ModelSerializer):
	# imageuser=serializers.StringRelatedField(many=True,read_only=True)
	imageuser=PostSerializer(many=True,read_only=True)
	class Meta:
		model=User
		fields=['id','username','first_name','last_name','email','password','imageuser']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Student
		fields=['id','url','name','roll','city']

class UserLoginSerializer(serializers.ModelSerializer):
	email=serializers.EmailField(max_length=255)
	class Meta:
		model=User
		fields=	['email','password']