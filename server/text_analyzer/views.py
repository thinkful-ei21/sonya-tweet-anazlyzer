from django.shortcuts import render
from django.http import HttpResponse


def analyze(request):
    # return a response containing the sentiment value for user's input search terms
    # if value:
    #     return HttpResponse()
    # else:
    #     return HttpResponseNotFound("<h1>Page not found</h1>")
    return HttpResponse("Analyze this")

