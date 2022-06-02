from django.shortcuts import render
from example.models import NewsItem

def index(request):
    data = NewsItem.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)
