from django.db import models
from questions.models import Question


class RepetitionPlan(models.Model):
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
        related_name='plan',
        verbose_name='Вопрос'
    )
    next_review_date = models.DateField(verbose_name='Дата следующего повторения')
    interval_days = models.IntegerField(default=1, verbose_name='Интервал (дни)')
    easiness_factor = models.FloatField(default=2.5, verbose_name='Коэффициент лёгкости')
    repetitions = models.IntegerField(default=0, verbose_name='Количество повторений')

    class Meta:
        verbose_name = 'План повторения'
        verbose_name_plural = 'Планы повторений'

    def __str__(self):
        return f'План: {self.question.text[:50]}'