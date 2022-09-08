from django.urls import path
from .views import SignUpView,HomeView
from .views import PostListView,CreatePost,UserDetailView,UpdatePostview,DeletePostview,MyPostView

urlpatterns=[
	path('', HomeView.as_view(), name='home'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('profile/',PostListView.as_view(),name="profile"),
	path('create/',CreatePost.as_view(),name='createpost'),
	path('detail/<int:pk>',UserDetailView.as_view(),name='Userdetail'),
	path('Update/<int:pk>',UpdatePostview.as_view(),name='Updatepost'),
	path('delete/<int:pk>',DeletePostview.as_view(),name='deletepost'),
	path('mypost/<int:pk>',MyPostView.as_view(),name='mypost'),
]