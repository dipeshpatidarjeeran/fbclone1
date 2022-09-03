from django.urls import path
from .views import SignUpView,HomeView
from .views import ProfileTemplate,CreatePost,PostDeleteView

urlpatterns=[
	path('', HomeView.as_view(), name='home'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('profile/',ProfileTemplate.as_view(),name="profile"),
	path('create/',CreatePost.as_view(),name='createpost'),
	#path('<int:Id>/',PostDeleteView.as_view(), name="deletedata"),
]