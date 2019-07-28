import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, "index/index.html")


def json_data(request):
    result = {"name": "Not Sure", "age": 25, "city": "深圳"}
    # return JsonResponse(result)
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")
