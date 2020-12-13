from django.shortcuts import render


def home(request):
    return render(request, 'index/home.html', {})


def sub(request):
    return render(request, 'index/sub.html', {})


def work(request):
    return render(request, 'index/experience.html', {})


def about(request):
    return render(request, 'index/about.html', {})


def projects(request):
    return render(request, 'index/projects.html', {})