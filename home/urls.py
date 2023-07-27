from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.home, name='home'),
    path('recomendations/', views.home_recomendations, name='home-recomendations'),
    path('content/<int:pk>/', views.Content.as_view(), name='content-id'),
    path('filter/<int:catID>/<slug:sort>/', views.home_filters, name='home-filters')
]