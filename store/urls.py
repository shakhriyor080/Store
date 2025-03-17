from django.urls import path
from . import views
urlpatterns = [
    path('', views.store , name='store'),
    path('search/', views.search_result, name='search_result'),
    path('/detail/<int:pk>/', views.products_detail, name='products_detail'),
    path('store/<int:pk>/leave-comment', views.leave_comment, name='leave_comment'),
 
 
]