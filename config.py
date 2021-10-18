import random
import core

dingtalk_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=d52e22e093a6e85459a7ff267fa410207891e5899c58e51436be9e6c67af6c2b'

weibo_search_url = 'http://s.weibo.com/weibo/'

西苑的大宝贝 = {
        '早上': {1: random.choice(core.shuffle(core.clone([3,4,5,6,7,8,9,10,11,12,13,14,15,16])))},
        
        '中午': {
               1: random.choice(core.shuffle(core.clone(list(range(1,25))))),
               2: random.choice(core.shuffle(core.clone(['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', '木桶饭', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13']))),
               3: random.choice(core.shuffle(core.clone(list(range(1,25))))),
              },
        
        '晚上':  {
               1: random.choice(core.shuffle(core.clone(list(range(1,25))))),
               2: random.choice(core.shuffle(core.clone(['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', '木桶饭', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13']))),
               3: random.choice(core.shuffle(core.clone(list(range(1,25))))),              
              },
        
        '休闲': {
               1: random.choice(core.shuffle(core.clone([6]))),
               2: random.choice(core.shuffle(core.clone([12]))),
               3: random.choice(core.shuffle(core.clone([13])))
              }
       }

东苑的大宝贝 = {
        '早上': {
               1: random.choice(core.shuffle(core.clone([1,2,3,4,5,6,7,8,9]))),
               2: random.choice(core.shuffle(core.clone([1,2,3,4,5,6,7,8,9,12,23,24]))),
               3: random.choice(core.shuffle(core.clone([1,3,5,7,9,11,13])))
               },
        
        '中午': {
               1: random.choice(core.shuffle(core.clone([1,2,5,7,8,9,12,17]))),
               2: random.choice(core.shuffle(core.clone([1,2,3,4,5,6,7,8,9,12,23,24]))),
               3: random.choice(core.shuffle(core.clone([1,3,5,7,9,11,13])))
              },
        
        '晚上':  {
               1: random.choice(core.shuffle(core.clone([1,2,5,7]))),
               2: random.choice(core.shuffle(core.clone([1,2,3,4,5,6,7,8,9,12,23,24]))),
               3: random.choice(core.shuffle(core.clone([1,3,5,7,9,11,13])))
              },
        
        '休闲': {
               1: random.choice(core.shuffle(core.clone([6]))),
               2: random.choice(core.shuffle(core.clone([12]))),
               3: random.choice(core.shuffle(core.clone([13])))
              }
       }

西苑黑名单 = [(2, 24), (3, 6), (3,7), (3, 11)]

东苑黑名单 = [(2, 5)]