from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView ,RedirectView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.views import generic	 
from .forms import NewUserForm,PostForm
from django.views import View
from django.contrib.auth.models import User
from .models import Post
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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
	
class CreatePost(LoginRequiredMixin,generic.CreateView):
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

class DeletePostview(DeleteView):
	model=Post
	success_url=reverse_lazy('profile')

class MyPostView(ListView):
	model=Post
	template_name='registration/mypost_list.html'


	
		