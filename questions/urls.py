from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_questions, name='import_questions'),
    path('<int:question_id>/ai/', views.generate_ai_answer, name='generate_ai_answer'),
]