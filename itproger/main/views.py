from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        "title": "Main Page!",
        "values": ["Word", 123, True, "Fourth"],
    }
    return render(
        request, "main/index.html", data
    )  # The actually way is "templates/main/index.html"


def about(request):
    return render(request, "main/about.html")


def other(request):
    return HttpResponse("<h2>All other not working urls</h2>")
