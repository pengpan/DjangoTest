import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, "index/index.html")


def json_data(request):
    result: json = {"name": "Not Sure", "age": 25, "city": "深圳"}
    # return JsonResponse(result)
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


@csrf_exempt
def post_request(request):
    body: json = json.loads(request.body)
    print(body)

    success: bool = False
    msg: str = ""
    if body["name"] == "":
        msg = "name cannot be empty."
    elif body["age"] == "":
        msg = "age cannot be empty."
    elif body["city"] == "":
        msg = "city cannot be empty."
    else:
        success = True

    return JsonResponse({"success": success, "msg": msg})
