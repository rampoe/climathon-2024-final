from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("article/list/", views.article_list, name="article_list"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
]
