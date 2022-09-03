from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView ,RedirectView
from django.urls import reverse_lazy,reverse
from django.views import generic	 
from .forms import NewUserForm,PostForm
from django.views import View
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
class HomeView(TemplateView):
	template_name='registration/home.html'

class SignUpView(generic.CreateView):
	form_class = NewUserForm
	success_url = reverse_lazy('login')
	template_name='registration/signup.html'

class ProfileTemplate(TemplateView):
	form_class=PostForm
	success_url=reverse_lazy('createpost')
	template_name='registration/profile.html'
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(**kwargs)
		posts=Post.objects.all()
		context={'pst':posts,}
		return context

class CreatePost(generic.CreateView):
	form_class=PostForm
	template_name='registration/createpost.html'
	success_url=reverse_lazy('profile')

class PostDeleteView(RedirectView):
	url='/'
	def get_redirect_url(self,*args,**kwargs):
		del_id=kwargs['id']
		Post.objects.get(pk=del_id).delete()
		return super().get_redirect_url(*args,**kwargs)




	
		