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

	def retrieve(self,request,pk=None):
		stu=Student.objects.get(pk=pk)
		serializer=StudentSerializer(stu)
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




class UserModelViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer


class PostModelViewSet(viewsets.ModelViewSet):
	queryset=Post.objects.all()
	serializer_class=PostSerializer


class UserloginAPI(APIView):
	serializer_class=LoginSerializer

	def post(self, request):
		username=request.data['username']
		password=request.data['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			token, created = Token.objects.get_or_create(user=user)
			return Response({'token': token.key})
		return Response({"error":"username and password does not match"})
		

class UserRegistrationAPI(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegistrationSerializer
	def post(self,request):
		serializer=self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"msg":"user registration successfully","data":serializer.data})


class UserLogout(APIView):
	permission_classes=[IsAuthenticated]
	def get(self,request,format=None):
		#import pdb;pdb.set_trace()
		request.user.auth_token.delete()
		logout(request)
		return Response({"msg":"logout user "})
		
