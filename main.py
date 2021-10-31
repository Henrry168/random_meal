import random
import urllib.parse
import time
import requests

import core
import config

from interval import Interval

now_localtime = time.strftime("%H:%M:%S", time.localtime())
print(now_localtime)
now_time = Interval(now_localtime, now_localtime)
time_interval_1 = Interval("7:00:00", "9:00:00")
time_interval_2 = Interval("11:00:00", "13:00:00")
time_interval_3 = Interval("17:00:00", "20:00:00")
if now_time in time_interval_1:
    time = '早上'
elif now_time in time_interval_2:
    time = '中午'
else:
    time = '晚上'


#窗口
def 吃什么好呢(time, 餐厅序号):
    destination = random.choice(core.shuffle(core.clone(list(config.餐厅[餐厅序号]['内容'][time].items()))))
    if destination in config.餐厅[餐厅序号]['内容']['黑名单']:
        吃什么好呢(time, 餐厅序号)
    else:
        destination
    floor, number = destination
    去餐厅 = config.学校 + config.餐厅[餐厅序号]['名字'] + str(floor) + '楼' + str(number) + '号'
    print(destination)
    return 去餐厅


#def 微博():
    global 西苑微博
    item_xiyuan = 去餐厅
    西苑url = urllib.parse.quote(item_xiyuan)
    西苑微博 = config.weibo_search_url + 西苑url


def 一言():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    res = requests.get('https://v1.hitokoto.cn/', headers=headers)
    return res.json()["hitokoto"] + '——' + res.json()["from"]


def 最终文本():
    #微博()
    时间 = '现在时刻，北京时间' + str(now_time)
    问候 = '大家好，今天' + time + '的幸运窗口是：' + '\n'
    文本 = ''
    for i in range(2):
        叫号 = 吃什么好呢(time, i)
        文本 = 文本 + 叫号 + '\n'

    最终文本 = 时间 + '\n\n' + 问候 + 文本 + '\n' + \
        '请收下食堂菌的一言，不要介意哟：' + '\n' + 一言()
    print(最终文本)
    return 最终文本


最终文本()