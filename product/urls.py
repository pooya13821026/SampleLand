from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<str:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<cat>', views.ProductListView.as_view(), name='product_categories_list'),
    path('brand/<br>', views.ProductListView.as_view(), name='product_brands_list'),
    path('search/', views.search, name='search'),
]
