from django.shortcuts import render
from .models import Task

def home(request):
    query = request.GET.get('name')
    if query:
        tasks = Task.objects.filter(name__icontains=query)
    else:
        tasks = Task.objects.all()
    return render(request, 'index.html', {"tasks": tasks})