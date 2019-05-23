from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.SET_DEFAULT, default=1, related_name='comments')
    user = models.CharField(max_length=250)
    email = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user






#add  in thumbnail later
#add in author later

#python manage.py makemigrations
#python manage.py makemigrations
#use the upper two commands whenever you make changes in the model
#whenever we make channges to the models when need to migrate kit
#11 theres alway error when you migrate so the fix is simply to add "on_delete=models.PROTECT"


#we create a snippet which is a model whose function is to cut the number of words to let say 100
#to add ... at the end
#9 blank = true beacuse the if a doesnt want to upload anythingits ok
