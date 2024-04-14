from django.urls import path
from . import views
app_name='item'
urlpatterns=[
  path('newitem/',views.newitem,name='newitem'),
  path('<int:pk>/',views.detail,name='detail'),
  ]