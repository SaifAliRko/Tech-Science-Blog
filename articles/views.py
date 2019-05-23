from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .import forms



def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })

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






#this variable 'articles' saves all objects in Article and by .order by it sorts it by
#field date which is already an element in models.py under Article

 #third parameter in this render function is the data that we want to send to the view
#or template,inside curly brackets we write a Dictionary,"articles" is the property here,whereas the articles on the right is articles on the 7th line,
#this Dictionary will be sended to the template
#so when we render line 9 we display at the output  the data
#we cature that slug vairable and use it  in url.py url of slug
    # return HttpResponse(slug)
