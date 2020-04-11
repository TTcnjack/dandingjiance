from django.shortcuts import render

# Create your views here.
import time
import datetime
import json
import redis
# import dingtalk
import requests
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from django_redis import get_redis_connection
from danding.views import home
from common.redis_pool import Pool
from common import config
from common.func import find_one_down, find_down, _to_chinese4


def login(request):
    if request.method == "POST":
        # print(request.body)
        data_code = json.loads(request.body)
        # print('code is %s', code)
        code = data_code.get("code")

        return HttpResponse(1)
    return render(request, 'base/base_main.html')

