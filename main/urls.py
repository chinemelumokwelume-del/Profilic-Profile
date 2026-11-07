from django.urls import path
from . import views

urlpatterns = [
    path('', views.enter, name='main_enter'),
    path('login/', views.enter, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]
