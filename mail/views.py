from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, resident_id):
    return HttpResponse("You're looking at resident id %s." % resident_id)


from django.shortcuts import render

# Create your views here.
