from rest_framework import serializers
from .models import Student,Post
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
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



class LoginSerializer(serializers.ModelSerializer):
	username = serializers.CharField(required=False)
	password = serializers.CharField(required=True, style={"input_type": "password"})
	class Meta:
		model = User
		fields = ["username", "password"]
		# if User.objects.filter(username=username,password=password).exists():
		# 	return True
		# return False

class RegistrationSerializer(serializers.ModelSerializer):
	# user=serializers.CharField(max_length=70,validators=[UniqueValidator(queryset=User.objects.all())])
	# email=serializers.EmailField(max_length=70,validators=[UniqueValidator(queryset=User.objects.all())])
	password=serializers.CharField(write_only=True, required=True, validators=[validate_password])
	# password2=serializers.CharField(write_only=True, required=True)
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','password']

	# def validate(self,attrs):
	# 	if attrs['password']!= attrs['password2']:
	# 		raise serializers.ValidationError({'password':'password field did not match'})
	# 	return attrs

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