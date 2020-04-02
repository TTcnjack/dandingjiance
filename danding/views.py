from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def worker(request):
    return render(request, 'worker.html')

def worker_list(request):
    return render(request, 'worker_list.html')

def arguments(request):
    return render(request, 'arguments.html')