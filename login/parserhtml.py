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
                if key == 'action':
                    self.fields['action'] = value
                elif key == 'method':
                    self.fields['method'] = value
        elif tag == 'input':
            for key, value in attrs:
                if key == 'type':
                    self.submit['type'] = value
                elif key == 'onclick':
                    self.submit['onclick'] = value
        else:
            for key, value in attrs:
                if key == 'name':
                    self.fields['name'].append(value)

    # def handle_data(self, data):
    #     if self.form:
    #         self.data += data
    #     if self.data and not self.form:
    #         self.forms.append(self.data)
    #         self.data = ''


def get_html_form(html):
    return [i for i in re.findall(form_re, html)]


def find_login_form(lis):
    for i in lis:
        hp = HTMLForms()
        hp.feed(i)
        hp.close()
        if 'login' in hp.fields.get('action', ''):
            return hp


if __name__ == '__main__':
    import requests
    html = requests.get('http://www.maiziedu.com/').text
    forms = get_html_form(html)
    hp = HTMLForms()
    hp.feed(forms[1])
    hp.close()
    print hp.fields