"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from . import views

# pybo/views
from pybo.views import base_views
# home/views
from home.views import home_views

from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Web Ai Django API v1.0", default_version='v1',
      contact=openapi.Contact(email="rlawjddla0203@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'answer', views.AnswerViewSet)


urlpatterns = [
    # 시작 화면
    path('',home_views.main, name='main'),
    path('home/',include('home.urls')),
    # 게시글 화면
    path('index/',base_views.index, name='index'),
    # 관리자 
    path('admin/', admin.site.urls),
    # 게시글 관리
    path('pybo/', include('pybo.urls')),
    # 사용자 관리
    path('common',include('common.urls')),
    # allauth login 네네
    path('accounts/', include('allauth.urls')),
    # rest api
    path('restapi/', include(router.urls)),
    path('restapi/api-auth/',include('rest_framework.urls')),   
    # swagger, redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    

]
