import pytest
from django.contrib.auth.models import User
from subjects.models import Subject
from questions.models import Question
from planner.models import RepetitionPlan


@pytest.mark.django_db
def test_create_subject():
    user = User.objects.create(username='testuser')
    subject = Subject.objects.create(name='Python', user=user)
    assert subject.name == 'Python'
    assert subject.user == user


@pytest.mark.django_db
def test_create_question():
    user = User.objects.create(username='testuser')
    subject = Subject.objects.create(name='Python', user=user)
    question = Question.objects.create(
        subject=subject,
        text='Что такое Django?',
        answer='Web-фреймворк'
    )
    assert question.subject == subject
    assert 'Django' in question.text


@pytest.mark.django_db
def test_create_repetition_plan():
    user = User.objects.create(username='testuser')
    subject = Subject.objects.create(name='Python', user=user)
    question = Question.objects.create(
        subject=subject,
        text='Тест',
        answer='Ответ'
    )
    plan = RepetitionPlan.objects.create(
        question=question,
        next_review_date='2026-05-12',
        interval_days=1
    )
    assert plan.question == question
    assert plan.interval_days == 1
