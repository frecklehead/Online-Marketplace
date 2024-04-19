from django.urls import path
from . import views

app_name='chat'
urlpatterns=[
  path('<int:pk>/',views.detail,name='detail'),
  path('',views.inbox,name='inbox'),
  path('new/<int:item_pk>/', views.new_chats,name='new'),
]