from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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