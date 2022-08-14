from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {})

def new(request):
    return render(request, 'new.html', {})
