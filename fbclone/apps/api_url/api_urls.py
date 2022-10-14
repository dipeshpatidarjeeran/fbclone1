from django.urls import path,include
from api_view.api_views import StudentModelViewSet,PostModelViewSet,UserLogout,UserModelViewSet,UserloginAPI,UserRegistrationAPI
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#CREATE ROUTER OBJECT
router=DefaultRouter()

#register serializer class with router
router.register('studentapi',StudentModelViewSet,basename='student')
router.register('postapi',PostModelViewSet,basename='post')
router.register('userapi',UserModelViewSet,basename='user')

#swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API View",
      default_version='v1',
      description="API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns=[
	path('crud/',include(router.urls)),
	path('auth/',include('rest_framework.urls',namespace='rest_framework')),
	path("loginapi/", UserloginAPI.as_view(),name='loginapi'),
	path("logoutapi/", UserLogout.as_view(),name='logout'),
	path('register/', UserRegistrationAPI.as_view(), name='auth_register'),
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	#path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]