from django.urls import path
from . import views


urlpatterns = [
    path('ninja_login', views.ninja_login),
    path('ninja_gold', views.ninja_gold),
    path('process_money', views.process_money),
    path('reborn', views.reborn)
]