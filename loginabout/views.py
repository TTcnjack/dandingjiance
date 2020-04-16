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
from common import config, jwttoken
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
        # get_user_data_url = r"https://oapi.dingtalk.com/user/get?access_token={access_token}&userid={user_id}".format(
        #     access_token=access_token,
        #     user_id=get_people_msg.get('userid')
        # )
        # get_people_data = requests.get(url=get_user_data_url).json()

        print(get_people_msg)
        # get_people_msg = {
        #     'errcode': 0,
        #     'sys_level': 1,
        #     'is_sys': False,
        #     'name': '黄伟强',
        #     'errmsg': 'ok',
        #     'deviceId': 'af94337af4fda5eb46c9e4ee26d626eb',
        #     'userid': '305236686539711167'
        # }
        token_msg = jwttoken.gen_long_token(get_people_msg).decode()
        print(token_msg)

        return JsonResponse({"msg": "ok!", "data": token_msg, "sys_level": get_people_msg.get('sys_level')})
        # return redirect("home/")
    return render(request, 'base/base_main.html')


def home_ajax(request):

    time_data = time.time()
    conn = redis.Redis(connection_pool=Pool)
    #
    data2 = conn.lrange('all_machine', 0, 1)[0]
    # data2 = conn.lrange('run_rate_page', 0, 1)[0]
    data1 = json.loads(data2)

    return JsonResponse(data1)