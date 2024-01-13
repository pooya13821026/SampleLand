from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('change-pass/', views.ChangePass.as_view(), name='change_pass'),
    path('user-cart/', views.user_cart, name='user_cart'),
    path('delete-order-item', views.delete_from_order_items, name='delete_order_item'),
]
