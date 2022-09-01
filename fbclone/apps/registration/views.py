from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView 
from django.urls import reverse_lazy
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
	form_class=NewUserForm
	success_url=reverse_lazy('createpost','login')
	template_name='registration/profile.html'

class CreatePost(TemplateView):
	template_name='registration/createpost.html'
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(**kwargs)
		fm=PostForm()
		stud=Post.objects.all()
		context={'form':fm,'stu':stud}
		return context
	def post(self,request):
		fm=PostForm(request.POST)
		if fm.is_valid():
			fm.save()
	
		return HttpResponseRedirect('/')