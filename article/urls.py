from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    #path('create/', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add/', views.article_add, name="add"),
    path('detail/<int:id>', views.article_detail, name="detail"),
    path('edit/<int:id>', views.article_edit, name="edit"),
    path('delete/<int:id>', views.article_delete, name="delete"),
    path('index/', views.article_list, name="index"),
    path('', views.article_list, name="article_bos"),
    path('comment/<int:id>', views.article_comment, name="comment"),
]
