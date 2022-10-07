from django.shortcuts import render
from django.contrib.auth.models import User
from registration.models import Student,Post
from django.contrib.auth import authenticate
from registration.serializers import StudentSerializer,PostSerializer,UserSerializer,UserLoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView 
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	# permission_classes=[IsAuthenticatedOrReadOnly]

class UserModelViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer

class PostModelViewSet(viewsets.ModelViewSet):
	# import pdb;pdb.set_trace()
	queryset=Post.objects.all()
	serializer_class=PostSerializer

class UserLoginAPI(APIView):
	def post(self,request,format=None):
		serializer=UserLoginSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			email=serializer.data.get('email')
			password=serializer.data.get('password')
			user=authenticate(email=email,password=password)
			if user is not None:
				return Response({"msg":"login successfully"},status=status.HTTP_200_OK)
			else:
				return Response({"msg":{"non_fiels_error":['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)		





