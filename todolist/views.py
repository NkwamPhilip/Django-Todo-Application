from django.shortcuts import render

def index(request):
    return render(request, 'todolist/index.html')

def show(request):
    return render(request, 'todolist/show.html')
