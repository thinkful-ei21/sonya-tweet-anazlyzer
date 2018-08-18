from django.shortcuts import render
from django.http import HttpResponse, QueryDict, HttpResponseNotFound


def analyze(request):
    query = request.GET.get("search")
    print(query)
        # search_term = QueryDict["search"]
    return HttpResponse({"value": "Analyze this"})
    # else:
        # return HttpResponseNotFound("<h1>Page not found</h1>")
