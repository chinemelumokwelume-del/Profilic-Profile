from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='blog_page'),
    path('create/', views.post_create, name='blog_postcreate'),
    path('category_create/', views.category_create, name='blog_categorycreate'),
    path('post/<int:id>/', views.category_detail, name='blog_postdetail'),
    path('category/<int:id>/', views.category_detail, name='blog_categorydetail'),
]