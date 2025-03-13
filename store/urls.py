from django.urls import path
from . import views
urlpatterns = [
    path('', views.store , name='store'),
   
    path('/detail/<int:pk>/', views.products_detail, name='products_detail'),
 
 
]