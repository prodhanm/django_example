from django.urls import path
from auth import views

urlpatterns = [
    path('login_view/', views.login_view),
    path('logout_view/', views.logout_view, name="logout_view")
]