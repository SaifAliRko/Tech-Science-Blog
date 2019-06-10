from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import *

def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article)
    if request.method=="POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            Comment.objects.create(article=article, user=request.user, content=content)
            Comment.save()
            return HttpResponseRedirect(article.get_absolute_url())
    else:
        comment_form= CommentForm()


    context = {
        'article' : article,
        'comments' : comments,
        #'comment_form' : comment_form,
    }
    return render(request, 'articles/article_detail.html', context)

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })