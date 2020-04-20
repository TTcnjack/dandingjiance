import time
import datetime
import json
import redis
# import dingtalk
import requests
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django_redis import get_redis_connection
from django.core.cache import cache

from common.redis_pool import Pool
from common import config
from common.func import find_one_down, find_down, _to_chinese4
from common.jwttoken import auth, auth_token

# Create your views here.


def hee(request):
    return render(request, 'base/base_main.html')


def home(request):
    # username_redis = request.session.get("userid")
    # print('session is is %s', username_redis)
    time_data = time.time()
    # conn = redis.Redis(connection_pool=Pool)
    # #
    # data2 = conn.lrange('all_machine', 0, 1)[0]
    # # data2 = conn.lrange('run_rate_page', 0, 1)[0]
    # data1 = json.loads(data2)
    # cache.lpush("avbbc", "value")
    # a = cache.keys('*')
    # print(data1)
    # print(dict(data1))
    # if data2:
    #     data1 = json.loads(data2[0])
    # else:
    data1 = {
        "create_time": "-",
        "rt_run_rate": 99,
        "month_run_rate": -1,
        "shift_rt_weight": -1,
        "rt_break_rate": -1,
        "rt_weak_num": -1,
        "rt_empty_num": -1,
    }

    return render(request, 'home/home.html', {'data': data1})


def running_rate(request):
    conn = redis.Redis(connection_pool=Pool)
    running_data = conn.lrange('run_rate_page', 0, 1)[0]
    # print(running_data)
    data_list = []
    if running_data:
        datas = json.loads(running_data)
        machine_num = datas.get('num_of_machine')
        for i in range(machine_num):
            i_num = i+1
            machine_key = 'machine_{}'.format(str(i_num))
            mechine = datas.get(machine_key)
            data_list.append(mechine)
            # if mechine.get('status') is -1:
            #     machine_no_man = {
            #         "machine_id": i_num,
            #         "owner": "-",
            #         "status": "-",
            #         "shift_run_rate": "-",
            #         "month_run_rate": "-"}
            #     data_list.append(machine_no_man)
            # else:
            #     data_list.append(mechine)

    # machine_no_man = {
    #                 "machine_id": "02",
    #                 "owner": "jack",
    #                 "status": 1,
    #                 "shift_run_rate": "88",
    #                 "month_run_rate": "99"}
    #
    # data_list = [machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man,machine_no_man]
    return render(request, 'home/running_rate.html', {"datas": data_list})


def output(request):
    # machine_no_man = {
    #     "machine_id": "02",
    #     "owner": "jack",
    #     "type": "棉花",
    #     "daily_rt_weight": "89.5",
    #     "shift_rt_weight": "88",
    #     "month_rt_weight": "99"}

    conn = redis.Redis(connection_pool=Pool)
    weight_data = conn.lrange('weight_page', 0, 1)[0]
    data_list = []
    if weight_data:
        datas = json.loads(weight_data)
        machine_num = datas.get('num_of_machine')
        for i in range(machine_num):
            i_num = i + 1
            machine_key = 'machine_{}'.format(str(i_num))
            mechine = datas.get(machine_key)
            data_list.append(mechine)

    # data_list = [machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man,
    #              machine_no_man, machine_no_man,machine_no_man,machine_no_man]

    return render(request, 'home/output.html', {"datas": data_list})


def break_per(request):
    # machine_no_man = {
    #     "machine_id": "02",
    #     "owner": "jack",
    #     "rt_break_rate": "0.65",
    #     "month_break_rate": "89.5",
    # }

    conn = redis.Redis(connection_pool=Pool)
    break_rate_page = conn.lrange('break_rate_page', 0, 1)[0]
    data_list = []
    if break_rate_page:
        datas = json.loads(break_rate_page)
        machine_num = datas.get('num_of_machine')
        for i in range(machine_num):
            i_num = i + 1
            machine_key = 'machine_{}'.format(str(i_num))
            mechine = datas.get(machine_key)
            data_list.append(mechine)
    # data_list = [machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man,
    #              machine_no_man, machine_no_man,machine_no_man,machine_no_man]

    return render(request, 'home/break_per.html', {"datas": data_list})


def empty_ingot(request):
    # machine_no_man = {
    #     "machine_id": "02",
    #     "owner": "jack",
    #     "rt_empty_num": "2",
    # }
    conn = redis.Redis(connection_pool=Pool)
    empty_info_page = conn.lrange('empty_info_page', 0, 1)[0]
    data_list = []
    if empty_info_page:
        datas = json.loads(empty_info_page)
        machine_num = datas.get('num_of_machine')
        for i in range(machine_num):
            i_num = i + 1
            machine_key = 'machine_{}'.format(str(i_num))
            mechine = datas.get(machine_key)
            data_list.append(mechine)
    # data_list = [machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man,
    #              machine_no_man, machine_no_man, machine_no_man, machine_no_man]
    return render(request, 'home/empty_ingot.html', {"datas": data_list})


def weak_twist(request):
    machine_no_man = {
        "machine_id": "02",
        "owner": "jack",
        "rt_weak_num": "2",
        "month_weak_num": "10",
    }
    # conn = redis.Redis(connection_pool=Pool)
    # weak_info_page = conn.lrange('weak_info_page', 0, 1)[0]
    # data_list = []
    # if weak_info_page:
    #     datas = json.loads(weak_info_page)
    #     machine_num = datas.get('num_of_machine')
    #     for i in range(machine_num):
    #         i_num = i + 1
    #         machine_key = 'machine_{}'.format(str(i_num))
    #         mechine = datas.get(machine_key)
    #         data_list.append(mechine)

    data_list = [machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man,
                 machine_no_man, machine_no_man, machine_no_man, machine_no_man]
    return render(request, 'home/weak_twist.html', {"datas": data_list})

# @auth
def worker(request):
    # token = request.GET.get("token")
    # # print("token2 is %s", token)
    # err, msg, data = auth_token(token)
    # # print(data)
    # machine_no_man = {'name': data.get('name'), "id": data.get('userid')}
    # product_lists = []
    # conn = redis.Redis(connection_pool=Pool)
    # workers_list = conn.lrange('worker_output', 0, 1)[0]
    # if workers_list:
    #     datas = json.loads(workers_list)
    #     worker_num = datas.get('num_of_worker')
    #     product_list = datas.get('product_list')
    #     machine_no_man['product_list'] = product_list
    #     for i in range(worker_num):
    #         i_num = i + 1
    #         worker_key = 'worker_{}'.format(str(i_num))
    #         mechine = datas.get(worker_key)
    #         machine_no_man['ic_card'] = mechine.get('ic_card')
    #         if mechine.get('dingding_user_id') == data.get('userid'):
    #             for product in product_list:
    #                 product_lists.append(mechine.get(product))
    #             machine_no_man['product_lists'] = product_lists
    #     if "product_lists" not in machine_no_man:
    #         for product in product_list:
    #             product_lists.append(0)
    #         machine_no_man['product_lists'] = product_lists
    # print(machine_no_man)
    machine_no_man = {'name': '黄伟强', 'id': '305236686539711167', 'product_list': ['纯化纤', '纯棉纱', '涤棉纱', '棉粘纱', '准棉纱'], 'ic_card': '0x45c014df', 'product_lists': [0, 0, 0, 0, 0]}

    return render(request, 'worker/worker.html', {"datas": machine_no_man})

# @auth
def worker_list(request):

    # conn = redis.Redis(connection_pool=Pool)
    # workers_list = conn.lrange('worker_output', 0, 1)[0]
    # data_list = []
    #
    # if workers_list:
    #     datas = json.loads(workers_list)
    #     worker_num = datas.get('num_of_worker')
    #     product_list = datas.get('product_list')
    #     for i in range(worker_num):
    #         i_num = i + 1
    #         worker_key = 'worker_{}'.format(str(i_num))
    #         mechine = datas.get(worker_key)
    #         product_lists = []
    #         for product in product_list:
    #             product_lists.append(mechine.get(product))
    #         mechine['pro'] = product_lists
    #         data_list.append(mechine)

    # print(data_list)
    data_list=[{'ic_card': '0x45c014df', 'dingding_user_id': '1934420414803409', 'name': '戴帅', '纯化纤': 0.28, '纯棉纱': 0.0, '涤棉纱': 0.0, '棉粘纱': 0.0, '准棉纱': 0.0, 'pro': [0.28, 0.0, 0.0, 0.0, 0.0]}]
    product_list = ['纯化纤', '纯棉纱', '涤棉纱', '棉粘纱', '准棉纱']
    # return HttpResponse(1)
    return render(request, 'worker_list/worker_list.html', {"datas": data_list, "product_list": product_list})

@auth
def arguments(request):

    machine_no_man = {
        "machine_id": "02",
        "owner": "jack",
        "thick_count": "2",
        "k_value": "10",
        "wet_rate": "4.5",
        "front_roller_diameter": "2.2"
    }
    conn = redis.Redis(connection_pool=Pool)
    machine_param_page = conn.lrange('machine_param_page', 0, 1)[0]
    data_list = []
    if machine_param_page:
        datas = json.loads(machine_param_page)
        machine_num = datas.get('num_of_machine')
        for i in range(machine_num):
            i_num = i + 1
            machine_key = 'machine_{}'.format(str(i_num))
            mechine = datas.get(machine_key)
            data_list.append(mechine)

    # data_list = [machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man, machine_no_man,
    #              machine_no_man, machine_no_man, machine_no_man, machine_no_man]
    return render(request, 'arguments/arguments.html', {"datas": data_list})


def dingding(request):
    # 跟用户状态无关,每次访问都必须去获取当前的access_token,所以能简写不能省略
    if request.method == "POST":
        url = r"https://oapi.dingtalk.com/gettoken?appkey=ding0qsys3hwvuehgm3y&appsecret=Kj_irB0mNvxffh7zbwSMt-nEyKIG_9AueII0QfEn2G5drg_OO5qxw0cp5cx-KYGz"
        agent_id = 677118324
        data2 = json.loads(request.body)
        alarm_user_list = data2.get('alarm_user_list')
        totle_weak_num = data2.get('total_weak_num')
        # 总弱捻锭数大于0再发送
        if totle_weak_num >= 1:
            rt_weak_num_list = data2.get('rt_weak_num')
            today = time.time()
            timeArray = time.localtime(today)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            text = "---- 弱捻情况报告 ----\n" \
                   "时间：{time} \n" \
                   "总弱捻锭数：{num} \n".format(time=otherStyleTime, num=totle_weak_num)
            for rt in range(config.machine_num):
                rtnum = rt + 1
                num = _to_chinese4(rtnum)
                ding = rt_weak_num_list[rt]
                if ding is -1:
                    ding = "- (设备未在线)"
                ts = "设备{num}弱捻锭数：{ding} \n".format(num=num, ding=ding)
                text = text + ts
            print(alarm_user_list)
            acc = requests.get(url=url)
            access_token = acc.json().get('access_token')
            print('this token is %s', access_token)
            header_dict = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                "Content-Type": "application/json"
            }
            url2 = r'https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token={}'.format(access_token)
            print(text)
            data_post = {
                "agent_id": agent_id,
                "userid_list": alarm_user_list,
                "msg": {
                    "msgtype": "text",
                    "text": {
                        "content": text
                        }
                    }
                }
            print(access_token)
            print(url)
            pooo = requests.post(url=url2, headers=header_dict, data=json.dumps(data_post))
            # print(pooo.text)        else:
            pass

    return JsonResponse({"msg": "ok!"})


def test(request):
    return render(request, 'test.html')


def page_not_found(request, exception):

    context={
        'error':'404 Error'
    }
    return render(request, 'err/error_404.html')

def page_error(request):

    context={
        'error':'404 Error'
    }
    return render(request, 'err/error_404404.html')