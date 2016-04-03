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
                self.fields[key] = value
        elif tag == 'input':
            for key, value in attrs:
                if key == 'type':
                    self.submit['type'] = value
                elif key == 'onclick':
                    self.submit['onclick'] = value
                elif key == 'name':
                    self.fields['name'].append(value)


class AjaxLogin(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.fields = ['input', 'button']
        self.login_functions = list()

    def handle_starttag(self, tag, attrs):
        if tag in self.fields:
            if dict(attrs).has_key('onclick'):
                for key, value in attrs:
                    if 'login' in value:
                        self.login_functions.append(dict(attrs))


def find_ajax_login(text):
    li = list()
    a = AjaxLogin()
    a.feed(text)
    a.close()
    for i in a.login_functions:
        li.append(i.get('onclick', ''))
    return list(set(li))


def get_html_form(html):
    return [i for i in re.findall(form_re, html)]


def find_login_form(lis):
    login_froms = list()
    for i in lis:
        hp = HTMLForms()
        hp.feed(i)
        hp.close()
        if not hp.fields.get('action', ''):
            pass
        if 'login' in hp.fields.get('action', ''):
            login_froms.append(hp)
    return login_froms


def get_fields_to_login(index):
    forms = get_html_form(html)
    hps = find_login_form(forms)
    return (hp.fields['name'] for hp in hps)


def ajax_analyse(index):
    ajax_re = r'$ajax'


def find_log_info(index):
    info = dict()
    info['ajax_url'] = list()
    info['post_data'] = dict()
    return info


def test():
    test_file_path = '/home/hidden/Documents/www.html'
    html = open(test_file_path, 'r').read()
    print('get html ok')
    forms = get_html_form(html)
    hp = find_login_form(forms)
    print hp[0].fields


if __name__ == '__main__':
    test_file_path = '/home/hidden/Documents/www.html'
    html = open(test_file_path, 'r').read()
    a = AjaxLogin()
    a.feed(html)
    a.close()
