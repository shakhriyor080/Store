from django.urls import path
from . import views
urlpatterns = [
    path('', views.store , name='store'),
    path('category1/<slug:slug>/', views.category1_detail, name='category1_detail_url'),
    path('<slug>/detail', views.products_detail, name='products_detail'),
]