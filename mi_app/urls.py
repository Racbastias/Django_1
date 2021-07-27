from django.urls import path
from . import views


urlpatterns = [
    path('names/<str:name>', views.func3),
    path('dos/', views.func2),
    path('', views.root),
    path('blogs/', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/json', views.json)
]