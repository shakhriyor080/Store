from django.urls import path
from . import views
urlpatterns = [
    path('', views.store , name='store'),
    path('category1/<slug:slug>/', views.category1_detail, name='category1_detail_url'),
    path('store/<slug:slug>/', views.products_detail, name='products_detail'),
      path('register/', views.register, name='register'),
]