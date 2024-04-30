from django.urls import path
from . import views
app_name='dashboard'
urlpatterns=[
  path('',views.index,name='index'),
  path('daily-sales/', views.daily_sales_plot, name='daily_sales_plot'),
]
