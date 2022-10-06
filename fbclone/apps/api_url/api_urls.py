from django.urls import path,include
from api_view.api_views import StudentModelViewSet,PostModelViewSet,UserModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

#CREATE ROUTER OBJECT
router=DefaultRouter()

#register serializer class with router
router.register('studentapi',StudentModelViewSet,basename='student')
router.register('postapi',PostModelViewSet,basename='post')
router.register('userapi',UserModelViewSet,basename='user')

urlpatterns=[
	# path('crud/',StudentListCreate.as_view()),
	# path('crud/<int:pk>',Student_RUD.as_view()),
	path('crud/',include(router.urls)),
	path('auth/',include('rest_framework.urls',namespace='rest_framework')),
	path('gettoken/',obtain_auth_token),
]