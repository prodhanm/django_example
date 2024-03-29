from django.urls import path
from example import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('news_add/', views.news_add),
    path('author_add/', views.authoradd),
    path('likes/<int:id>/', views.like_view),
    path('news/edit/<int:id>/', views.news_edit),
]