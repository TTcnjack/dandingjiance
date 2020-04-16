import os
import random
import time
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect


def render_json(code=0, msg='null', data=None):
    return JsonResponse({'code': code, 'msg': msg, 'data': data})


def find_one_down(data_dict):

    for data_key, data_value in data_dict.items():
        if data_value is -1:
            data_dict[data_key] = '-'
        elif type(data_value) is float:
            data_dict[data_key] = str('%.1f' % data_value)
        else:
            pass

    return data_dict


def find_down(data_dict):

    for data_key, data_value in data_dict.items():

        if data_value is -1:
            data_dict[data_key] = None

        elif str(data_key).split("_")[-1] == "rate":

            data_dict[data_key] = '{:.2%}'.format(data_value)
        else:
            pass

    return data_dict


_MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七',u'十八', u'十九')
_P0 = (u'', u'十', u'百', u'千',)
_S4 = 10 ** 4


def _to_chinese4(num):

    assert (0 <= num and num < _S4)
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num / 10
        lst.append(num)
        c = len(lst)  # 位数
        result = u''

        for idx, val in enumerate(lst):
            val = int(val)
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
                if idx < c - 1 and lst[idx + 1] == 0:
                    result += u'零'
        return result[::-1]

print(type(_to_chinese4(5)))


# def auth(func):
#     def inner(request, *args, **kwargs):
#         # if not request.session.session_key:
#         #     request.session.create()
#         #     username_redis = request.session.get("userid")
#         #     print('userid is %s', username_redis)
#         if not request.session.get("userid"):
#             username_redis = request.session.get("userid")
#             print('userid is %s',username_redis)
#             return redirect('/')
#         return func(request, *args, **kwargs)
#     return inner