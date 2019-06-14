from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

    tags = TaggableManager()


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


class Comment(models.Model):
    article = models.ForeignKey(Article,  on_delete=models.PROTECT)
    user = models.ForeignKey(User,  on_delete=models.PROTECT)
    content = models.TextField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return '{}.{}'.format(self.article.title, str(self.user.username))

