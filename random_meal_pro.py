import requests
import json
import random
import urllib.parse
import time
from interval import Interval

now_localtime = time.strftime("%H:%M:%S", time.localtime())
now_time = Interval(now_localtime, now_localtime)
print(now_time)
time_interval_1 = Interval("7:00:00", "9:00:00")
time_interval_2 = Interval("11:00:00", "13:00:00")
time_interval_3 = Interval("17:00:00", "20:00:00")
if now_time in time_interval_1:
    meal = '早'
elif now_time in time_interval_2:
    meal = '午'
else:
    meal = '晚'
        
info = {
        '早': {1: random.choice(shuffle(clone([1,2,3,4,5,6,7,8,9])))},
        
        '午': {
               1: random.choice(shuffle(clone([1,2,5,7,8,9,12,17]))),
               2: random.choice(shuffle(clone([1,2,3,4,5,6,7,8,9,12,23,24]))),
               3: random.choice(shuffle(clone([1,3,5,7,9,11,13])))
              },
        
        '晚':  {
               1: random.choice(shuffle(clone([1,2,5,7]))),
               2: random.choice(shuffle(clone([1,2,3,4,5,6,7,8,9,12,23,24]))),
               3: random.choice(shuffle(clone([1,3,5,7,9,11,13])))
              },
        
        '休闲': {
               1: random.choice(shuffle(clone([6]))),
               2: random.choice(shuffle(clone([12]))),
               3: random.choice(shuffle(clone([13])))
              }
       }

黑名单 = [(3, 12)]

url = 'https://weibo.com/search/weibo?q='

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

def 发钉钉():
    url='https://oapi.dingtalk.com/robot/send?access_token=d52e22e093a6e85459a7ff267fa410207891e5899c58e51436be9e6c67af6c2b'
    program = {
        "msgtype": "text",
        "text": { "content": 文本}
        }
    headers={ 'content-Type' : 'application/json'}
    res = requests.post(url, data=json.dumps(program), headers=headers)


def 吃什么好呢(meal):
    global destination, floor, number, 去西苑
    destination = random.choice(shuffle(clone(list(info[meal].items()))))
    判断()
    floor, number = destination
    去西苑 =  '郑航西苑' + str(floor) + '楼' +  str(number) + '号'
    print(destination)
   
def 判断(): 
    if destination in 黑名单:
        吃什么好呢()
    else:
        return destination

def 微博():
    global 西苑微博
    item_xiyuan = 去西苑
    西苑url = urllib.parse.quote(item_xiyuan)  
    西苑微博 = url + 西苑url

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
    吃什么好呢('早')
    微博()
    时间 = '现在时刻，北京时间' + str(now_time)
    问候 = '大家好，今天' + meal + '上' + '的幸运窗口是：'
    文本 = 时间 + '\n\n' + 问候 + 去西苑 + '\n' + '来看看这里有什么吧: ' + str(西苑微博) + '\n' + '\n' + '您还可以选择：东苑' + '\n' + '来看看这里有什么吧: 哎呀！这里什么也没有，真不好意思呢。' + '\n\n' + '请收下食堂菌的一言，不要介意哟：' + '\n' + content_yiyan
      
最终文本()
发钉钉()
