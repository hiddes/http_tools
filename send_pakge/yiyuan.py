# -- coding:utf8 -- #
import requests
import json

APIKey = '05ff921caf568e4c018d9538f91f7d97'
joke_url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page='


def parse_json(result):
    d = json.loads(result)
    if d.get('showapi_res_code') == 0:
        data = d.get('showapi_res_body')
        if data.get('ret_code') == 0:
            return data.get('contentlist')


def get_jokes(page=1):
    headers = dict(apikey=APIKey)
    try:
        req = requests.get(url=''.join((joke_url, str(page))), headers=headers)
    except Exception, e:
        print e
        return []
    else:
        if req.status_code == 200:
            return parse_json(req.text)
        else:
            return []


if __name__ == '__main__':
    text = get_jokes(2)
    for i in text:
        print i.get('title')
        print i.get('text')
