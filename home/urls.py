from django.urls import path, include
from .views import home_views

app_name = 'home'

urlpatterns = [
    # base_views.py
    path('',
         home_views.main, name='main'),
]