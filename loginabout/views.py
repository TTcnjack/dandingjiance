import time
import datetime
import json
import redis
import requests
import hashlib

from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from django_redis import get_redis_connection
from django.core import signing
from django.core.cache import cache

from danding.views import home
from common.redis_pool import Pool
from common import config
from common.func import find_one_down, find_down, _to_chinese4
from common.my_token import *

def login(request):
    if request.method == "POST":
        data_code = json.loads(request.body)
        code = data_code.get("code")
        url = r"https://oapi.dingtalk.com/gettoken?appkey=ding0qsys3hwvuehgm3y&appsecret=Kj_irB0mNvxffh7zbwSMt-nEyKIG_9AueII0QfEn2G5drg_OO5qxw0cp5cx-KYGz"

        acc = requests.get(url=url)
        access_token = acc.json().get('access_token')
        get_token_url = r'https://oapi.dingtalk.com/user/getuserinfo?access_token={access_token}&code={code}'.format(
            access_token=access_token, code=code)
        get_people_msg = requests.get(url=get_token_url).json()
        print(get_people_msg)
        get_people_msg ={
                    "userid": "65455218922",
                    "sys_level": 1,
                    "errmsg": "ok",
                    "is_sys": "true",
                    "errcode": 0
                }


        token_msg = create_token(get_people_msg.get('userid'))
        # request.session['username'] = get_people_msg.get('name')
        # request.session['userid'] = get_people_msg.get('userid')
        # request.session['sys_level'] = get_people_msg.get('sys_level')
        # username_redis = request.session.get("userid")
        # print(username_redis)

        return JsonResponse({"msg": "ok!", "data": token_msg, "sys_level": get_people_msg.get('sys_level')})
        # return redirect("home/")
    return render(request, 'base/base_main.html')

