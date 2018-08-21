from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
import json
from services import analyzer


def analyze(request):
    if request.method == "GET":
        print("request fired")
        q = request.GET.get("search")
        anal = analyzer()
        sentiment = anal.analyze_tweets(q)
        data = {
            "search": q,
            "sentiment": sentiment
        }
        # string = "<h1> What up? </h1>"
        # print(JsonResponse(data))
        # return JsonResponse(string, safe=False)
        # response = HttpResponse(data)
        # response["Access-Control-Allow-Origin"] =  "*"
        # return response
        return JsonResponse(data)
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")
