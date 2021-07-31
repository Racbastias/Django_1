from django.urls import path
from . import views


urlpatterns = [
    path('random', views.random_page),
    path('reset', views.reset),
    path('login', views.login),
]