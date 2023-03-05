from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def all_articles(request):
    return HttpResponse('<h4> Всички публикации </h4>')


