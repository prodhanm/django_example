from django.urls import path
from auth import views

urlpatterns = [
    path('login_view/', views.login_view)
]