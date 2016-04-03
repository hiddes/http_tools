# -- coding:utf8 -- #

import requests
import traceback

from parserhtml import get_fields_to_login


def get_index_html(url):
    try:
        req = requests.get(url)
    except requests.ConnectionError:
        print traceback.extract_stack()
        return None
    else:
        if req.status_code == 200:
            return req.text


def test(index, user, passwd):
    get_fields_to_login(index)


if __name__ == '__main__':
    url = 'http://www.maiziedu.com'
    html = get_index_html(url)
    hp = HTMLForms()
    hp.feed(html)
    print hp.forms
