from django.contrib import admin
from django.urls import path

from .views import emailView, successView

urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sendemail.urls')), # new
]
