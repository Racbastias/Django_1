from django.urls import path
from . import views


urlpatterns = [
    path('ninja_login', views.ninja_login),
    path('ninja_gold', views.ninja_gold),
    path('ninja_values', views.ninja_values),
    path('process_money', views.process_money),
    path('ninja_rules', views.ninja_rules),
    path('reborn', views.reborn),
    path('exit', views.exit)
]