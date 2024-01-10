from django.urls import path

from simple_blog.articles import views

urlpatterns = [
    path('articles/', views.index, name='articles_index'),
]
