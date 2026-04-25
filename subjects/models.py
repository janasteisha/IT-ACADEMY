from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subjects',
        verbose_name='Владелец'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['-created_at']

    def __str__(self):
        return self.name