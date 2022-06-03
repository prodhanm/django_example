from django.shortcuts import render, reverse, HttpResponseRedirect
from example.models import NewsItem
from example.forms import NewsAddForm

def index(request):
    data = NewsItem.objects.all()
    html = "index.html"
    context = {'data': data}
    return render(request, html, context)

def news_add(request):
    html = "newsaddform.html"
    if request.method == "POST":
        form = NewsAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            NewsItem.objects.create(
                title=data['title'],
                body=data['body'],
                author=data['author']
            )
            return HttpResponseRedirect('/')
    form = NewsAddForm()
    context = {"form": form}
    return render(request, html, context)