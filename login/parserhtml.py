# -- coding:utf8 -- #

from HTMLParser import HTMLParser
import re

form_re = re.compile(r'<form[\s\S]*?</form>')

html = '''
'''


class HTMLForms(HTMLParser):
    """
    test
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self.fields = dict()
        self.submit = dict()
        self.fields['name'] = []

    def handle_starttag(self, tag, attrs):
        if tag == 'form':
            for key, value in attrs:
                self.fields['action'] = value
        elif tag == 'input':
            for key, value in attrs:
                if key == 'type':
                    self.submit['type'] = value
                elif key == 'onclick':
                    self.submit['onclick'] = value
                elif key == 'name':
                    self.fields['name'].append(value)
                    # else:
                    #     for key, value in attrs:
                    #         if key == 'name':
                    #             self.fields['name'].append(value)


def get_html_form(html):
    return [i for i in re.findall(form_re, html)]


def find_login_form(lis):
    login_froms = list()
    for i in lis:
        hp = HTMLForms()
        hp.feed(i)
        hp.close()
        if 'login' in hp.fields.get('action', ''):
            login_froms.append(hp)
    return login_froms


if __name__ == '__main__':
    import requests

    html = requests.get('http://www.maiziedu.com/').text
    forms = get_html_form(html)
    hp = find_login_form(forms)

    print hp[0].fields
