from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict, HttpResponseNotFound
import json

def analyze(request):
    if request.method == "GET":
        # print("request fired")
        # q = request.GET.get("search")
        # data = {
        #     "search": q,
        #     "name": "sonya"
        # }
        # print(data)
        # return JsonResponse(data)
        response = HttpResponse("Here's the text of the Web page.")
        response = HttpResponse("Text only, please.", content_type="text/plain")
        return response
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")
