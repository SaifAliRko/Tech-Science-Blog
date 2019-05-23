from django.conf.urls import url
from  .import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),


]

#?P<slug> this whole thing a name capturing group
#\w is anynumber or any alphabet then - then + for any length and then $ for end
#7 naming so that all may be different eg naming = list
#8 #here we get slug from views.py and use here
