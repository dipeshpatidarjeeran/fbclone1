from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView ,RedirectView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.views import generic	 
from .forms import NewUserForm,PostForm
from django.views import View
from django.contrib.auth.models import User
from .models import Post
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
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
	def get_context_date(self,*args,**kwargs):
		stuff=get_object_or_404(Post,id=self.kwargs['pk'])
		total_likes=stuff.num_liked()
		context['total_likes']=total_likes
		return context
	
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

def LikePostView(request,pk):
	post=get_object_or_404(Post,id=request.POST.get('post_id'))
	post.liked.add(request.user)
	return HttpResponseRedirect(reverse('mypost',args=[str(pk)]))