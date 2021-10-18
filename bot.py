import requests
import config
import json

def dingtalk(text):
    program = {
        "msgtype": "text",
        "text": { "content": text}
        }
    headers={ 'content-Type' : 'application/json'}
    res = requests.post(config.dingtalk_webhook, data=json.dumps(program), headers=headers)