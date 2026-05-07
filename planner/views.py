from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import RepetitionPlan
from questions.models import Question


def today_review(request):
    today = timezone.now().date()
    plans = RepetitionPlan.objects.filter(next_review_date__lte=today)
    
    return render(request, 'planner/review.html', {
        'plans': plans,
        'today': today
    })


def rate_question(request, plan_id):
    if request.method == 'POST':
        plan = get_object_or_404(RepetitionPlan, id=plan_id)
        quality = int(request.POST.get('quality', 3))
        
        # Алгоритм SM-2
        match quality:
            case q if q < 3:  # Сложно
                plan.interval_days = 1
                plan.easiness_factor = max(1.3, plan.easiness_factor - 0.2)
            case 3:  # Нормально
                plan.interval_days = max(1, round(plan.interval_days * plan.easiness_factor))
            case _:  # Легко (4 или 5)
                plan.interval_days = max(1, round(plan.interval_days * plan.easiness_factor * 1.3))
                plan.easiness_factor += 0.1
        
        plan.repetitions += 1
        plan.next_review_date = timezone.now().date() + timezone.timedelta(days=plan.interval_days)
        plan.save()
        
        return redirect('today_review')
    
    return redirect('today_review')