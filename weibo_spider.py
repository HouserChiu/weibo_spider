'''
微博手机版比网页版容易爬，少了很多渲染
‘https://m.weibo.cn/’
'''

import requests
import json
import pprint


response = requests.get('https://m.weibo.cn/comments/hotflow?id=4478465341975128&mid=4478465341975128&max_id_type=0')
data = json.loads(response.text)
#pprint格式化打印
pprint.pprint(data)
users = data['data']['data']

for user in users:
    print(user['text'])
    print(user['user']['id'])
    print(user['user']['screen_name'])