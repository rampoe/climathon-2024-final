from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    image = models.ImageField(upload_to="article_images/", blank=True, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    body = models.TextField(verbose_name=_("Body"))
