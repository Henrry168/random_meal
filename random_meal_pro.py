import requests
import json
import random
import urllib.parse
import time
from interval import Interval
from config import 西苑的大宝贝
from config import 东苑的大宝贝
from config import 西苑黑名单
from config import 东苑黑名单
from config import url

now_localtime = time.strftime("%H:%M:%S", time.localtime())
now_time = Interval(now_localtime, now_localtime)
print(now_time)
time_interval_1 = Interval("7:00:00", "9:00:00")
time_interval_2 = Interval("11:00:00", "13:00:00")
time_interval_3 = Interval("17:00:00", "20:00:00")
if now_time in time_interval_1:
    meal = '早上'
elif now_time in time_interval_2:
    meal = '中午'
else:
    meal = '晚上'

def clone(self):
    result = []
    for i in range(1000):
        for x in self:
            result.append(x)
    
    return result

def shuffle(lis):
    result = []
    while lis:
        p = random.randrange(0, len(lis))
        result.append(lis[p])
        lis.pop(p)
    return result
        
微博url = 'http://s.weibo.com/weibo/'

def 发钉钉():
    program = {
        "msgtype": "text",
        "text": { "content": 文本}
        }
    headers={ 'content-Type' : 'application/json'}
    res = requests.post(url, data=json.dumps(program), headers=headers)


def 吃什么好呢(meal):
    global destination, floor, number, 去西苑
    print(list(西苑的大宝贝[meal].items()))
    destination = random.choice(shuffle(clone(list(西苑的大宝贝[meal].items()))))
    判断()
    floor, number = destination
    去西苑 =  '郑航西苑' + str(floor) + '楼' +  str(number) + '号'
    print(destination)
   
def 判断():
    if destination in 西苑黑名单:
        吃什么好呢(meal)
    else:
        return destination

def 微博():
    global 西苑微博
    item_xiyuan = 去西苑
    西苑url = urllib.parse.quote(item_xiyuan)  
    西苑微博 = 微博url + 西苑url

def 一言():
    global content_yiyan
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
        }
    res = requests.get('https://v1.hitokoto.cn/', headers=headers)
    saying = res.json()["hitokoto"]
    writer = res.json()["from"]
    content_yiyan = saying + '\n' + '                                                                             ————' + writer

def 最终文本():
    global 文本
    一言()
    吃什么好呢(meal)
    微博()
    时间 = '现在时刻，北京时间' + str(now_time)
    问候 = '大家好，今天' + meal + '的幸运窗口是：'
    文本 = 时间 + '\n\n' + 问候 + 去西苑 + '\n' + '来看看这里有什么吧: ' + str(西苑微博) + '\n' + '\n' + '您还可以选择：东苑' + '\n' + '（东苑正在完善，别催了，555 o(╥﹏╥)o）' + '\n\n' + '请收下食堂菌的一言，不要介意哟：' + '\n' + content_yiyan
      
最终文本()
发钉钉()