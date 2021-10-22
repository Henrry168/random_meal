import random
import urllib.parse
import time
import requests

import core
import config

from interval import Interval

now_localtime = time.strftime("%H:%M:%S", time.localtime())
now_time = Interval(now_localtime, now_localtime)
time_interval_1 = Interval("7:00:00", "9:00:00")
time_interval_2 = Interval("11:00:00", "13:00:00")
time_interval_3 = Interval("17:00:00", "20:00:00")
if now_time in time_interval_1:
    meal = '早上'
elif now_time in time_interval_2:
    meal = '中午'
else:
    meal = '晚上'


def 吃什么好呢(meal):
    global destination, floor, number, 去西苑
    destination = random.choice(core.shuffle(
        core.clone(list(config.西苑的大宝贝[meal].items()))))
    判断()
    floor, number = destination
    去西苑 = '郑航西苑' + str(floor) + '楼' + str(number) + '号'
    print(destination)


def 判断():
    if destination in config.西苑黑名单:
        吃什么好呢(meal)
    else:
        return destination


def 微博():
    global 西苑微博
    item_xiyuan = 去西苑
    西苑url = urllib.parse.quote(item_xiyuan)
    西苑微博 = config.weibo_search_url + 西苑url


def 一言():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    res = requests.get('https://v1.hitokoto.cn/', headers=headers)
    return res.json()["hitokoto"] + '————' + res.json()["from"]


def 最终文本():
    global 文本
    吃什么好呢(meal)
    微博()
    时间 = '现在时刻，北京时间' + str(now_time)
    问候 = '大家好，今天' + meal + '的幸运窗口是：'
    return 时间 + '\n\n' + 问候 + 去西苑 + '\n' + '\n' + '您还可以选择：东苑' + '\n' + '（东苑正在完善，别催了，555 o(╥﹏╥)o）' + \
        '\n\n' + '请收下食堂菌的一言，不要介意哟：' + '\n' + 一言()


