from django.urls import path,include
from api_view.api_views import StudentModelViewSet,PostModelViewSet,UserLogout,UserModelViewSet,UserloginAPI,UserRegistrationAPI
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

#CREATE ROUTER OBJECT
router=DefaultRouter()

#register serializer class with router
router.register('studentapi',StudentModelViewSet,basename='student')
router.register('postapi',PostModelViewSet,basename='post')
router.register('userapi',UserModelViewSet,basename='user')

# router.register('login',UserloginAPI,basename='login')

urlpatterns=[
	path('crud/',include(router.urls)),
	path('auth/',include('rest_framework.urls',namespace='rest_framework')),
	path("loginapi/", UserloginAPI.as_view(),name='loginapi'),
	path("logout/", UserLogout.as_view(),name='logout'),
	path('register/', UserRegistrationAPI.as_view(), name='auth_register'),
	#path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]