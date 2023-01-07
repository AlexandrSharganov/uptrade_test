from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'menu_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('v2/', views.index_second, name='index_second'),
    path('v2/<int:pk>/', views.index_second, name='index_second_item'),
    path('<int:pk>/', views.index, name='menu_app_name')
]
