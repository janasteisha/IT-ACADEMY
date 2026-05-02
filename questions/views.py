from django.shortcuts import render
from .models import Question
from subjects.models import Subject

def import_questions(request):
    subjects = Subject.objects.all()
    
    if request.method == 'POST' and request.FILES.get('file'):
        subject_id = request.POST.get('subject')
        file = request.FILES['file']
        
        content = file.read().decode('utf-8')
        lines = content.strip().split('\n')
        
        count = 0
        for line in lines:
            parts = line.split(';')
            if len(parts) >= 2:
                Question.objects.create(
                    subject_id=subject_id,
                    text=parts[0].strip(),
                    answer=parts[1].strip()
                )
                count += 1
        
        return render(request, 'questions/import_result.html', {
            'count': count,
            'subject_id': subject_id
        })
    
    return render(request, 'questions/import_form.html', {
        'subjects': subjects
    })