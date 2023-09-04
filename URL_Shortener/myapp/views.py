from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, Spidey!")

def home_page(request):
    return render(request, "index.html")

def task_view(request):
    data = {
        'name': 'Ganesh Kumar C',
        'age': 21,
    }
    return render(request, 'task.html', context=data)