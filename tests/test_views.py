import pytest
from django.test import Client
from django.contrib.auth.models import User
from subjects.models import Subject


@pytest.mark.django_db
def test_subject_list_view():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_subject_detail_view():
    client = Client()
    user = User.objects.create(username='testuser')
    subject = Subject.objects.create(name='Python', user=user)
    response = client.get(f'/subjects/{subject.id}/')
    assert response.status_code == 200
    assert 'Python' in response.content.decode()


@pytest.mark.django_db
def test_import_page():
    client = Client()
    response = client.get('/questions/import/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_review_page():
    client = Client()
    response = client.get('/review/today/')
    assert response.status_code == 200
