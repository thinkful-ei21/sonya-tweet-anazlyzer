from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
import json


def analyze(request):
    if request.method == "GET":
        # print("request fired")
        # q = request.GET.get("search")
        data = {
            "search": "Trump",
            "name": "sonya"
        }
        # string = "<h1> What up? </h1>"
        # print(JsonResponse(data))
        # return JsonResponse(string, safe=False)
        response = HttpResponse(data)
        response["Access-Control-Allow-Origin"] =  "*"
        return response
        # return JsonResponse(response, safe=False)
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")
