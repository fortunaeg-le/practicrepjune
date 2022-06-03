from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    post = models.TextField(
        verbose_name='текст поста',
        help_text='текст поста',
    )
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name='дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Автор'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
