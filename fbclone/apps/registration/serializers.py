from rest_framework import serializers
from .models import Student,Post,Comment
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .utils import Util
class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Comment
		fields=['post','user','content','created_on']


class PostSerializer(serializers.ModelSerializer):
	comments=CommentSerializer(many=True,read_only=True)
	class Meta:
		model=Post
		fields=['id','photo','title','discription','comments']	


class UserSerializer(serializers.ModelSerializer):
	# imageuser=serializers.StringRelatedField(many=True,read_only=True)
	post=PostSerializer(many=True,read_only=True)
	class Meta:
		model=User
		fields=['id','username','first_name','last_name','email','password','post']


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Student
		fields=['id','name','roll','city']


class LoginSerializer(serializers.ModelSerializer):
	username = serializers.CharField(required=True)
	#email = serializers.EmailField(required=True)
	password = serializers.CharField(required=True, style={"input_type": "password"})
	class Meta:
		model = User
		fields = ["username","password"]
	# def validate(self,attrs):
	# 	email=attrs.get('email')
	# 	data={
	# 		"subject":"send mail",
	# 		"body":"user Login successfully",
	# 		"to_email":email
	# 	}
	# 	Util.send_email(data)
	# 	print('send mail')
	# 	return attrs

class RegistrationSerializer(serializers.ModelSerializer):
	# user=serializers.CharField(max_length=70,validators=[UniqueValidator(queryset=User.objects.all())])
	email=serializers.EmailField(max_length=70,validators=[UniqueValidator(queryset=User.objects.all())])
	password=serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2=serializers.CharField(write_only=True, required=True)

	class Meta:
		model=User
		fields=['username','first_name','last_name','email','password','password2']

	def validate(self,attrs):
		email=attrs.get('email')
		data={
			"subject":"send mail",
			"body":"user registration successfully",
			"to_email":email
		}
		Util.send_email(data)
		print('send mail')
		return attrs
		if attrs['password']!= attrs['password2']:
			raise serializers.ValidationError({'password':'password field did not match'})
		return attrs

	def create(self, validated_data):
		user = User(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			email=validated_data['email'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

