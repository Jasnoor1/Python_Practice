from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.UserCreate.as_view(), name='account-create'),
    path('login/', views.login),
]