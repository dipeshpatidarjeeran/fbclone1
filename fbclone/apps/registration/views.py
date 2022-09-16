from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView ,RedirectView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.views import generic	 
from .forms import NewUserForm,PostForm
from django.views import View
from django.contrib.auth.models import User
from .models import Post,Like
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
import json
# Create your views here.
class HomeView(TemplateView):
	template_name='registration/home.html'

class SignUpView(generic.CreateView):
	form_class = NewUserForm
	success_url = reverse_lazy('login')
	template_name='registration/signup.html'

class PostListView(ListView):
	model=Post
	success_url=reverse_lazy('createpost')
	template_name='registration/profile.html'
	
	
class CreatePost(generic.CreateView):
	model=User
	form_class=PostForm
	template_name='registration/createpost.html'
	success_url=reverse_lazy('profile')
	def form_valid(self,form):
		obj = form.save(commit=False)
		obj.author=self.request.user
		obj.save()
		return super().form_valid(form)

class UserDetailView(DetailView):
	model=User
	template_name='registration/user_detail.html'
	context_object_name='details'

class UpdatePostview(UpdateView):
	model=Post
	form_class=PostForm
	template_name='registration/UpdatePost.html'
	success_url=reverse_lazy('profile')
	def get_queryset(self):
		user = self.request.user
		return Post.objects.filter(author=user)
		
class DeletePostview(DeleteView):
	model=Post
	success_url=reverse_lazy('profile')
	def get_queryset(self):
		user = self.request.user
		return Post.objects.filter(author=user)
		
class MyPostView(ListView):
	model=Post
	template_name='registration/mypost_list.html'
	def get_queryset(self):
		user = self.request.user
		return Post.objects.filter(author=user)
	
	
class ShowImageDetail(DetailView):
	model=Post
	template_name='registration/showImage.html'
	context_object_name='showimage'

class UpdateProfileView(UpdateView):
	model=User
	fields=['username','first_name','last_name','email']
	template_name='registration/UpdateProfile.html'
	success_url=reverse_lazy('profile')
	def get_queryset(self):
		user = self.request.user
		return User.objects.filter(username=user)	

class NotValidView(TemplateView):
	template_name='registration/notvaliduser.html'

def like_PostView(request):
	user=request.user
	if request.method=='POST':
		mypost_id=request.POST.get('mypost_id')
		mypost_obj=Post.objects.get(id=mypost_id)
		current_likes=mypost_obj.likes
		if user in mypost_obj.likes.all():
			mypost_obj.likes.remove(user)
			current_likes=current_likes-1
		else:
			mypost_obj.likes.add(user)
			current_likes=current_likes+1
		mypost_obj.likes=current_likes
		mypost_obj.save()
		like,created=Like.objects.get_or_create(user=user,post_id=mypost_id)
		if not created:
			if like.value=='like':
				like.value='Unlike'
			else:
				like.value='like'
		like.save()
		return redirect('like_post')
