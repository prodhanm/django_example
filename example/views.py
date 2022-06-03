from django.shortcuts import render, reverse, HttpResponseRedirect
from example.models import NewsItem
from example.forms import NewsAddForm, AuthorAddForm

def index(request):
    data = NewsItem.objects.all()
    html = "index.html"
    context = {'data': data}
    return render(request, html, context)

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
def authoradd(request):
    html = "author_add.html"
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = AuthorAddForm()
    context = {"form": form}
    return render(request, html, context)