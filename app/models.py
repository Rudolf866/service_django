from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    text = models.TextField(verbose_name="Текст")
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        db_table = "post"
