from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('forget-password/', views.ForgetPassView.as_view(), name='forget_password'),
    path('reset-password/<active_code>', views.ResetPassView.as_view(), name='reset_password'),
    path('activate-account/<email_activate_code>', views.ActiveEmailAccountView.as_view(), name='activate_account'),
]
