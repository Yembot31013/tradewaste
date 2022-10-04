from django.urls import path

from recycle import scavenger
from . import views, authview, post

urlpatterns = [
  path('', views.home, name= "home"),
  path('about/<int:id>/', views.about, name= "about"),
  path('post', views.post, name= "post"),
  path('comment', views.comments, name= "comment"),
  path('register/', authview.register, name="register"),
  path('login/', authview.loginpage, name="loginpage"),
  path('logout/', authview.logoutpage, name="logoutpage"),
  path('scavenger/', views.scavenger, name="scavenger"),
  path('create_scavenger/', scavenger.index, name="create_profile"),
  path("call_someone", views.call_someone),
  path("add_work/<str:longitude>/<str:latitude>", views.add_work),
  path("receive", views.receive),
  path("suggestion", post.index, name="suggestion"),
  path("likes", post.add_likes, name="add_likes"),
]
