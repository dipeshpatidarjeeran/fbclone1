from django.contrib.auth.models import User
from registration.models import Student,Post
from registration.serializers import StudentSerializer,PostSerializer,UserSerializer,LoginSerializer,RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView 
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token
from registration.utils import Util

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	# permission_classes=[IsAuthenticatedOrReadOnly]
	
	def create(self, request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data) 

	def retrieve(self,request,*args,**kwargs):
		stu=self.get_objects()
		serializer=self.get_serializer(stu)
		return Response(serializer.data)

	def update(self, request,pk):
		stu=Student.objects.get(pk=pk)
		serializer = StudentSerializer(stu,data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)

	def destroy(self,request,pk):
		stu=Student.objects.get(pk=pk)
		stu.delete()
		return Response({"msg":'data deleted '})

	# def get_queryset(self):
	# 	import pdb;pdb.set_trace()
	# 	stu=self.request.user
	# 	return Student.objects.filter(name=user)




class UserModelViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer


class PostModelViewSet(viewsets.ModelViewSet):
	queryset=Post.objects.all()
	serializer_class=PostSerializer


class UserloginAPI(APIView):
	serializer_class=LoginSerializer
	queryset=User.objects.all()
	def post(self, request,*args,**kwargs):
		serializer=self.serializer_class(data=request.data)
		username=request.data['username']
		email=request.data['email']
		password=request.data['password']
		user=authenticate(request,username=username,email=email,password=password)
		if user is not None:
			login(request,user)
			token, created = Token.objects.get_or_create(user=user)
			body=username+"  Your token is "+str(token)
			#send mail
			data={
				"subject":"login mail",
				"body":body,
				"to_email":email
				}
			Util.send_email(data)
			return Response({'token': token.key})
		return Response(serializer.errors)
		

class UserRegistrationAPI(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegistrationSerializer
	def post(self,request):
		serializer=self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"msg":"user registration successfully","data":serializer.data})
		return Response(serializer.errors)

class UserLogout(APIView):
	permission_classes=[IsAuthenticated]
	def get(self,request,format=None):
		#import pdb;pdb.set_trace()
		request.user.auth_token.delete()
		logout(request)
		return Response({"msg":"logout user "})
		
