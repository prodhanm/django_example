from django.shortcuts import render
from example.models import NewsItem

def index(request):
    data = NewsItem.objects.all()
    html = "index.html"
    context = {'data': data}
    return render(request, html, context)
