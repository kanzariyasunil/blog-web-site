from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home,name = 'Home'),
    path('about', views.about,name = 'about'),
    path('contact', views.contect,name = 'contect'),
    path('search', views.search,name = 'search'),
    path('signup', views.handleSignup,name = 'handleSignup'),
    path('login',views.handlelogin,name = 'handlelogin'),
    path('logout',views.handlelogout,name = 'handlelogout')
]
