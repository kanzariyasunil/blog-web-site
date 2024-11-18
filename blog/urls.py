from django.urls import path
from . import views
urlpatterns = [
    path('postComment',views.postComment,name = 'postComment'),
    path('', views.bloghome,name = 'Home'),
    path('<str:slug>',views.blogpost,name = 'blogpost'),
    
]