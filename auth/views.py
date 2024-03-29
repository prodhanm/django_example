from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

from auth.forms import LoginForm

def login_view(request):
    html = "loginview.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ''' The user object is the code used to match username and 
            password.'''
            user = authenticate(
                request, 
                username=data["username"],
                password=data["password"]
            )
            if user:
                ''' The login is the function call and the user object
                is the variable defined under the if statement.'''
                login(request, user)
                ''' The return code is stating that if the user is
                not logged in, then redirect them to the next parameter,
                rather than the reverse parameter.'''
                return HttpResponseRedirect(request.POST.get("next", reverse("homepage")))
    form = LoginForm()
    context = {"form": form}
    return render(request, html, context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("logout_view"))
