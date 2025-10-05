from django.shortcuts import render
from django.http import HttpResponse

def index(request ):
    return HttpResponse('<h2>Testing my work</h2>')

def about(request ):
    return HttpResponse('<h2>About my work</h2>')

def other(request ):
    return HttpResponse('<h2>All other not working urls</h2>')
