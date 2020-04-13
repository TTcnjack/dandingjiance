import redis
import random
import time
import json

from redis_pool import Pool


def num_of01():
    num_of_machine = random.randint(0, 2)
    return num_of_machine


def num_of10():
    num_of_machine = random.randint(1, 10)
    return num_of_machine


def num_of100():
    rate = random.uniform(50, 100)
    return rate


def num_of300():
    num = random.randint(50, 300)
    return num


def type_is():
    types = random.choice(['纯纤维', '纯棉花', '纤维'])
    return types


def get_time():
    today = time.time()
    timeArray = time.localtime(today)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def all_machine():
    all_machines = {
        "create_time": get_time(),
        "rt_run_rate": num_of100(),
        "month_run_rate": num_of100(),
        "shift_rt_weight": num_of100(),
        "rt_break_rate": num_of100(),
        "rt_weak_num": num_of300(),
        "rt_empty_num": num_of300(),
    }
    return all_machines


def run_rate_pages():
    num_of_machine = num_of10()
    run_rate_page = {

            'create_time': get_time(),
            'num_of_machine': num_of_machine,


    }
    for i in range(num_of_machine):
        i_id = i+1
        machine_id = "machine_{}".format(i_id)
        run_rate_page[machine_id] = {
                                        "machine_id": i_id,
                                        'owner': "jack",
                                        'status': num_of01(),
                                        'shift_run_rate': num_of100(),
                                        'month_run_rate': num_of100()
                                    }
    return run_rate_page


def weak_info_pages():
    num_of_machine = num_of10()
    run_rate_page = {

            'create_time': get_time(),
            'num_of_machine': num_of_machine,


    }
    for i in range(num_of_machine):
        i_id = i+1
        machine_id = "machine_{}".format(i_id)
        run_rate_page[machine_id] = {
                                        "machine_id": i_id,
                                        'owner': "jack",
                                        'rt_weak_num': num_of10(),
                                        'month_weak_num': num_of10(),
                                    }
    return run_rate_page


def weight_pages():
    num_of_machine = num_of10()
    run_rate_page = {

            'create_time': get_time(),
            'num_of_machine': num_of_machine,


    }
    for i in range(num_of_machine):
        i_id = i+1
        machine_id = "machine_{}".format(i_id)
        run_rate_page[machine_id] = {

            "machine_id": i_id,
            'owner': "jack",
            'type': type_is(),
            'daily_rt_weight': num_of100(),
            'shift_rt_weight': num_of100(),
            'month_rt_weight': num_of100()
                                    }
    return run_rate_page


def send_redis():
    conn = redis.Redis(connection_pool=Pool)
    conn.lpush("all_machine", json.dumps(all_machine()))
    conn.lpush("run_rate_page", json.dumps(run_rate_pages()))
    conn.lpush("weak_info_page", json.dumps(weak_info_pages()))
    conn.lpush("weight_page", json.dumps(weight_pages()))


if __name__ == '__main__':
    while True:
        send_redis()
        time.sleep(5)
        print('1')