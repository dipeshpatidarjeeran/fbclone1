from django.urls import path
from .views import SignUpView,HomeView
from .views import PostListView,CreatePost,UserDetailView,UpdatePostview,DeletePostview,MyPostView,ShowImageDetail
from .views import UpdateProfileView,NotValidView,like_PostView
urlpatterns=[
	path('', HomeView.as_view(), name='home'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('profile/',PostListView.as_view(),name="profile"),
	path('create/',CreatePost.as_view(),name='createpost'),
	path('detail/<int:pk>',UserDetailView.as_view(),name='Userdetail'),
	path('Update/<int:pk>',UpdatePostview.as_view(),name='Updatepost'),
	path('delete/<int:pk>',DeletePostview.as_view(),name='deletepost'),
	path('mypost/<int:pk>',MyPostView.as_view(),name='mypost'),
	path('showimage/<int:pk>',ShowImageDetail.as_view(),name='showimagedetail'),
	path('updateProfile/<int:pk>',UpdateProfileView.as_view(),name='updateprofile'),
	path('notvalid/',NotValidView.as_view(),name='notvalid'),
	path('like/',like_PostView,name='like_post'),
]