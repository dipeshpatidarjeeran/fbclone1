from django.shortcuts import render
from django.contrib.auth.models import User
from registration.models import Student,Post
from registration.serializers import StudentSerializer,PostSerializer,UserSerializer
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
	authentication_classes=[SessionAuthentication]
	permission_classes=[IsAuthenticated]
	# permission_classes=[IsAuthenticatedOrReadOnly]

class UserModelViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer

class PostModelViewSet(viewsets.ModelViewSet):
	queryset=Post.objects.all()
	serializer_class=PostSerializer



# class StudentAPIViewSet(viewsets.ViewSet):
# 	def list(self,request):
# 		stu=Student.objects.all()
# 		serializer=StudentSerializer(stu,many=True)
# 		return Response(request.data)
# 	def retrieve(self,request,pk=None):
# 		id=pk
# 		stu=Student.objects.get(pk=id)
# 		serializer=StudentSerializer(stu)
# 		return Response(request.data)
# 	def create(self,request):
# 		serializer=StudentSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# 	def update(self,request,pk):
# 		id=pk
# 		stu=Student.objects.get(pk=id)
# 		serializer=StudentSerializer(stu,data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg':'data Updated'})
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# 	def prtial_update(self,request,pk):
# 		id=pk
# 		stu=Student.objects.get(pk=id)
# 		serializer=StudentSerializer(stu,data=request.data,partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg':'data  partial Updated'})
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# 	def destroy(self,request,pk):
# 		id=pk
# 		stu=Student.objects.get(pk=id)
# 		stu.delete()
# 		return Response({"msg":'data deleted '})






# class StudentListCreate(ListCreateAPIView):
# 	queryset=Student.objects.all()
# 	serializer_class=StudentSerializer

# class Student_RUD(RetrieveUpdateDestroyAPIView):
# 	queryset=Student.objects.all()
# 	serializer_class=StudentSerializer


# list and create data pk not requered
# class StudentListCreate(ListModelMixin,CreateModelMixin,GenericAPIView):
# 	queryset=Student.objects.all()
# 	serializer_class=StudentSerializer
# 	def get(self,request,*args,**kwargs):
# 		return self.list(request,*args,**kwargs)

# 	def post(self,request,*args,**kwargs):
# 		return self.create(request,*args,**kwargs)
# #retrieve update delete data pk requered
# class Student_RUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
# 	queryset=Student.objects.all()
# 	serializer_class=StudentSerializer
# 	def get(self,request,*args,**kwargs):
# 		return self.retrieve(request,*args,**kwargs)

# 	def put(self,request,*args,**kwargs):
# 		return self.update(request,*args,**kwargs)

# 	def delete(self,request,*args,**kwargs):
# 		return self.destroy(request,*args,**kwargs)




# class student_api(APIView):
# 	def get(self,request,format=None,pk=None):
# 		id=pk
# 		if id is not None:
# 			stu=Student.objects.get(id=id)
# 			serializers=StudentSerializer(stu)
# 			return Response(serializers.data)
# 		stu=Student.objects.all()
# 		serializer=StudentSerializer(stu,many=True)
# 		return Response(serializer.data)

# 	def post(self,request,format=None):
# 		serializer=StudentSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({"msg":"data created"},status=status.HTTP_201_CREATED)

# 	def put(self,request,pk,format=None):
# 		id=pk
# 		stu=Student.objects.get(pk=id)
# 		serializer=StudentSerializer(stu,data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({"msg":' complete data Updated'})
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 	def patch(self,request,pk,format=None):
# 		id=pk
# 		stu=Student.objects.get(pk=id)
# 		serializer=StudentSerializer(stu,data=request.data,partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({"msg":' partial data Updated'})

# 	def delete(self,request,pk,format=None):
# 		id=pk
# 		stu=Student.objects.get(pk=id)
# 		stu.delete()
# 		return Response({'msg':'data deleted'})


