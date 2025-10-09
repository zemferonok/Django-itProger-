from django.urls import path, re_path
from . import views
 
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    re_path(r'^.*$', views.other),
]
