from django.shortcuts import render

from . import models


def home_page(request):
    return render(request, "pages/home.html")


def about_page(request):
    return render(request, "pages/about.html")


def article_list(request):
    articles = models.Article.objects.all()
    return render(
        request,
        "pages/article_list.html",
        {"articles": articles},
    )
