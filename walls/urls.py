from django.urls import path
from . import views

urlpatterns = [
    path('', views.walls, name = 'walls'),
    path('compilation/', views.compilation, name = 'compilation')
]