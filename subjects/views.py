from django.shortcuts import render

def subject_list(request):
    return render(request, 'subjects/list.html')