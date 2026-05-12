from django.shortcuts import render
from .models import Question
from subjects.models import Subject
from planner.models import RepetitionPlan
from django.utils import timezone

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
                question = Question.objects.create(
                    subject_id=subject_id,
                    text=parts[0].strip(),
                    answer=parts[1].strip()
                )
                # Автоматически создаём план повторений для каждого вопроса
                RepetitionPlan.objects.create(
                    question=question,
                    next_review_date=timezone.now().date(),
                    interval_days=1,
                    easiness_factor=2.5,
                    repetitions=0
                )
                count += 1
        
        return render(request, 'questions/import_result.html', {
            'count': count,
            'subject_id': subject_id
        })
    
    return render(request, 'questions/import_form.html', {
        'subjects': subjects
    })


from django.http import JsonResponse
from app.ai_agent.services import AIAgent

def generate_ai_answer(request, question_id):
    question = Question.objects.get(id=question_id)
    agent = AIAgent()
    ai_answer = agent.generate_answer(question.text, question.subject.name)
    return JsonResponse({
        'question': question.text,
        'correct_answer': question.answer,
        'ai_answer': ai_answer
    })