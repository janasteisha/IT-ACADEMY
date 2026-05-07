from django.urls import path
from . import views

urlpatterns = [
    path('today/', views.today_review, name='today_review'),
    path('<int:plan_id>/rate/', views.rate_question, name='rate_question'),
]