from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
import json
from .services import Analyzer

anal = Analyzer()
def analyze(request):
    if request.method == "GET":
        print("request fired")
        q = request.GET.get("search")
        anal = Analyzer()
        sentiment = anal.analyze_tweets(q)
        data = {
            "search": q,
            "sentiment": sentiment
        }
        return JsonResponse(data)
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")
