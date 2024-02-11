from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    body = models.TextField(verbose_name=_("Body"))
