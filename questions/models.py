from django.db import models
from subjects.models import Subject


class Question(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Предмет'
    )
    text = models.TextField(verbose_name='Текст вопроса')
    answer = models.TextField(verbose_name='Правильный ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-created_at']

    def __str__(self):
        return self.text[:80]