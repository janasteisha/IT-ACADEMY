from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_questions, name='import_questions'),
]