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
from django.urls import path, include

from pybo import views as pybo_views

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Questions', views.QuestionViewSet)
router.register(r'Answers', views.AnswerViewSet)


urlpatterns = [
    # 시작 화면
    path('',pybo_views.index, name='index'),
    # 관리자 
    path('admin/', admin.site.urls),
    # 게시글 관리
    path('pybo/', include('pybo.urls')),
    # 사용자 관리
    path('common',include('common.urls')),
    # rest api
    path('restapi/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]
