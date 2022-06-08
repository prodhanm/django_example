from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import example

from example.models import NewsItem
from example.forms import NewsAddForm, AuthorAddForm

def index(request):
    data = NewsItem.objects.all()
    html = "index.html"
    context = {'data': data}
    return render(request, html, context)

@login_required
def news_add(request):
    html = "newsaddform.html"
    # Initiates a post request.
    if request.method == "POST":
        # takes in information over a post request.
        form = NewsAddForm(request.POST)
        # validates a post request.
        if form.is_valid():
            data = form.cleaned_data
            # Fills the form
            NewsItem.objects.create(
                title=data['title'],
                body=data['body'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse("homepage"))
    # This is a get request.
    form = NewsAddForm()
    context = {"form": form}
    return render(request, html, context)

def news_edit(request, id):
    news = NewsItem.objects.get(id=id)
    if request.method == "POST":
        form = NewsAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            news.title = data['title'],
            news.body = data['body'],
            news.author = data['author']
            news.save()
            return HttpResponseRedirect(reverse("homepage"))
            # args=(id,) is used in terms of a detail page that passes an id.
    '''Any information from the model, or more so, pertinent information
    can go here on the get request, as a way to edit those information.'''    
    form = NewsAddForm(initial={
        "title": news.title,
        "body": news.body,
        "author": news.author.id
    })
    context = {"form": form}
    return render(request, "newsaddform.html", context)

# This is the function for model form.
@login_required
def authoradd(request):
    html = "author_add.html"
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = AuthorAddForm()
    context = {"form": form}
    return render(request, html, context)

def like_view(request,id):
    post = NewsItem.objects.get(id=id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("homepage"))
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) , kwargs={'id': id}