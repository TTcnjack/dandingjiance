import time
import json
import redis
# import dingtalk
import requests
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django_redis import get_redis_connection

from common.redis_pool import Pool
# from common.func import render_json

# Create your views here.


def home(request):
    time_data = time.time()
    data = {
        "create_time": time_data,
        "rt_run_rate": 80,
        "month_run_rate": '95',
        "shift_rt_weight": '200',
        "rt_break_rate": '0.01',
        "rt_weak_num": '5',
        "rt_empty_num": '8',

    }
    conn = redis.Redis(connection_pool=Pool)

    data2 = conn.lrange('all_machine', 0, 1)
    print(data2)
    if data2:
        data = json.loads(data2[0])
    else:
        data = {
            "create_time": "-",
            "rt_run_rate": "-",
            "month_run_rate": '-',
            "shift_rt_weight": '-',
            "rt_break_rate": '-',
            "rt_weak_num": '-',
            "rt_empty_num": '-',
        }
    return render(request, 'home/home.html', {'data': data})


def running_rate(request):
    conn = redis.Redis(connection_pool=Pool)
    running_data = conn.lrange('run_rate_page', 0, 1)[0]
    data_list = []
    if running_data:
        datas = json.loads(running_data)
        machine_num = datas.get('num_of_machine')
        for i in range(machine_num):
            i_num = i+1
            machine_key = 'machine_{}'.format(str(i_num))
            mechine = datas.get(machine_key)
            if mechine.get('status') is -1:
                machine_no_man = {
                    "machine_id": i_num,
                    "owner": "-",
                    "status": "-",
                    "shift_run_rate": "-",
                    "month_run_rate": "-"}
                data_list.append(machine_no_man)
            else:
                data_list.append(mechine)
    return render(request, 'home/running_rate.html', {"datas": data_list})


def output(request):
    return render(request, 'home/output.html')


def break_per(request):
    return render(request, 'home/break_per.html')


def empty_ingot(request):
    return render(request, 'home/empty_ingot.html')


def weak_twist(request):
    return render(request, 'home/weak_twist.html')


def worker(request):
    return render(request, 'worker.html')


def worker_list(request):
    return render(request, 'worker_list.html')


def arguments(request):
    return render(request, 'arguments.html')


def dingding(request):
    if request.method == "POST":
        url = r"https://oapi.dingtalk.com/gettoken?appkey=ding0qsys3hwvuehgm3y&appsecret=Kj_irB0mNvxffh7zbwSMt-nEyKIG_9AueII0QfEn2G5drg_OO5qxw0cp5cx-KYGz"
        agent_id = 677118324
        data2 = json.loads(request.body)
        alarm_user_list = data2.get('alarm_user_list')[0]
        acc = requests.get(url=url)
        access_token = acc.json().get('access_token')
        print('this token is %s', access_token)
        header_dict = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"
        }
        # url = r'https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token={}&agent_id={}&userid_list={}'.format(access_token, agent_id, alarm_user_list)
        url2= r'https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token={}'.format(access_token)
        data_post = {
            # "access_token": access_token,
            "agent_id": agent_id,
            "userid_list": alarm_user_list,
            "msg": {
            "msgtype": "text",
            "text": {
                "content": "提示提示提示!!!!!!!!"
            }
        }
        }
        print(access_token)
        print(url)
        pooo = requests.post(url=url2, headers=header_dict, data=json.dumps(data_post))
        print(pooo.text)

    return JsonResponse({"msg": "ok!"})

