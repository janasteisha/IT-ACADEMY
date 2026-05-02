from django.shortcuts import render
from .models import Subject

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects': subjects})

def subject_detail(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    questions = subject.questions.all()
    return render(request, 'subjects/detail.html', {
        'subject': subject,
        'questions': questions
    })