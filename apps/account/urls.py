

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('sign-up/', views.sign_up, name='sign-up'),
]
