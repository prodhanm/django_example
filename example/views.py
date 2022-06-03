from django.shortcuts import render
from example.models import NewsItem
from example.forms import NewsAddForm

def index(request):
    data = NewsItem.objects.all()
    html = "index.html"
    context = {'data': data}
    return render(request, html, context)

def news_add(request):
    html = "newsaddform.html"
    form = NewsAddForm()
    context = {"form": form}

    return render(request, html, context)