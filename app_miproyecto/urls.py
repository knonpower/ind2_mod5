from django.urls import path
from . import views

app_name = 'app_miproyecto'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('app/', views.imagenes, name='imagenes'),
    path('app1/', views.index2, name='index2')
]