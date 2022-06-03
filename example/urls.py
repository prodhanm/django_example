from django.urls import path
from example import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('news_add/', views.news_add), 
]