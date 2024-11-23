from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.add_blog, name='add_blog'),
    path('delete/<int:post_id>/', views.delete_blog, name='delete_blog'),
]
