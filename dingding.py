import requests
import config
import json
import main


def dingtalk(text):
    program = {
        "msgtype": "text",
        "text": {"content": text}
    }
    headers = {'content-Type': 'application/json'}
    requests.post(item, data=json.dumps(program), headers=headers)

for item in config.Webhook:
    dingtalk(main.最终文本())