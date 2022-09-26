from django.urls import path
from .views import SignUpView,HomeView
from .views import PostListView,CreatePost,UserDetailView,UpdatePostview,DeletePostview,MyPostView,ShowImageDetail
from .views import UpdateProfileView,NotValidView,like_PostView,AddCommentView,DeleteCommentView
from django.contrib.auth import views 
urlpatterns=[
	path('', HomeView.as_view(), name='home'),
	#path('/logout/',logoutuser.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('profile/',PostListView.as_view(),name="profile"),
	path('create/',CreatePost.as_view(),name='createpost'),
	path('detail/<int:pk>',UserDetailView.as_view(),name='Userdetail'),
	path('Update/<int:pk>',UpdatePostview.as_view(),name='Updatepost'),
	path('delete/<int:pk>',DeletePostview.as_view(),name='deletepost'),
	path('deletecomment/<int:pk>',DeleteCommentView.as_view(),name='deletecomment'),
	path('mypost/<int:pk>',MyPostView.as_view(),name='mypost'),
	path('showimage/<int:pk>',ShowImageDetail.as_view(),name='showimagedetail'),
	path('updateProfile/<int:pk>',UpdateProfileView.as_view(),name='updateprofile'),
	path('notvalid/',NotValidView.as_view(),name='notvalid'),
	path('like/',like_PostView,name='like_post'),
	path('comment/',AddCommentView,name='add_comment'),
]