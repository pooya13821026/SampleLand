from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles'),
    path('category/<str:category>', views.ArticlesView.as_view(), name='articles_with_category'),
    path('send-comment', views.send_comment, name='send_comment'),
    path('<str:slug>', views.ArticleDetailView.as_view(), name='article_details'),
]
