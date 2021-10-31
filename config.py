import random
import core


weibo_search_url = 'http://s.weibo.com/weibo/'

bot = {
    'dingtalk':  'https://oapi.dingtalk.com/robot/send?access_token=d52e22e093a6e85459a7ff267fa410207891e5899c58e51436be9e6c67af6c2b'
}

学校 = '郑航'


# 此为自定义的变量，可删除
xi = {
    1: random.choice(core.shuffle(core.clone(list(range(1, 25))))),
    2: random.choice(core.shuffle(core.clone(['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11木桶饭', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13']))),
    3: random.choice(core.shuffle(core.clone(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']))),
}
dong = {
    1: random.choice(core.shuffle(core.clone([1, 2, 5, 7, 8, 9, 12, 17]))),
    2: random.choice(core.shuffle(core.clone([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 24]))),
    3: random.choice(core.shuffle(core.clone(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']))),
}
# 此为自定义的变量，可删除


餐厅 = [
    {
        '名字': '西苑',
        '内容':
        {
            '早上': {1: random.choice(core.shuffle(core.clone(['3 温馨粥道', '88（4） 逍遥镇胡辣汤', '5 葱花饼肉夹馍','6 姐弟俩土豆粉（麦香馅饼）','7 拌面（酱香饼）','9 曹状元烧饼','10 一品粥','11 油饼母鸡汤','12 上海生煎','13 卤肉饭','15 山西油泼面（肠粉）','16 荞麦面（大包子）','18 武汉小笼包','19 逍遥镇胡辣汤','21 大盘鸡面（酱香饼）','99（24） 掉渣饼'])))},

            '中午': xi,

            '晚上': xi,

            '休闲': {
                1: random.choice(core.shuffle(core.clone([6]))),
                2: random.choice(core.shuffle(core.clone([12]))),
                3: random.choice(core.shuffle(core.clone([13])))
            },
            '黑名单': [(2, 24), (3, 6), (3, 7), (3, 11)]
        }
    },

    {
        '名字': '东苑',
        '内容':
        {
            '早上': {1: random.choice(core.shuffle(core.clone([1, 2, 3, 4, 5, 6, 7, 8, 9])))},

            '中午': dong,

            '晚上': dong,

            '休闲': {
                1: random.choice(core.shuffle(core.clone([6]))),
                2: random.choice(core.shuffle(core.clone([12]))),
                3: random.choice(core.shuffle(core.clone([13])))
            },
            '黑名单': [(2, 5)]
        }
    }
]