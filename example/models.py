from django.db import models
from django.utils import timezone
'''For the purpose of this exercise, the User model here, 
is being tied to the authentication code and the model itself,
to where the User's data is tied to everything securely. This is
a fairly simple way to tie data of a User to their authentication.'''
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=50)
    '''The OneToOne field is used to ensure that a user is tied to
    one author and that everything of that one author is tied to the 
    author/user. There can not be any other user to a user profile. 
    This also means deleting our migrations and database to create an integrity
    of the data, or risk the data being error ridden. We need to recreate
    our superuser. This model also ensures that the author is tied to the user.
    Ex. The author Mustafa Prodhan is the user ie superuser, mustafa.'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title