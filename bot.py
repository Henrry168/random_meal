import requests
import config
import json


def dingtalk(text):
    program = {
        "msgtype": "text",
        "text": {"content": text}
    }
    headers = {'content-Type': 'application/json'}
    requests.post(config.bot.dingtalk, data=json.dumps(
        program), headers=headers)
