# -- coding:utf8 -- #
import smtplib
import socket
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import Message

__auto__ = u'俗子'


def check_mail_service(mail, server=0, ssl=0):
    port_list = [25, 465]
    company_mail = [None, 'exmail.qq.com']
    server_name = mail.split('@')[1]
    print(server_name)
    try:
        if company_mail[server] is None:
            smtp = smtplib.SMTP(''.join(('smtp.', server_name)), port_list[ssl], timeout=5)
        else:
            smtp = smtplib.SMTP(''.join(('smtp.', company_mail[server])), port_list[ssl], timeout=5)
    except socket.timeout:
        return check_mail_service(mail, server + 1)
    else:
        return smtp


def add_attach_p(msg, file_path):
    assert os.path.isdir(file_path)

    def add_file(*fi):
        for i in fi[2]:
            att = MIMEText(open(''.join((fi[1], i)), 'rb').read(), 'base64')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename='+i
            msg.attach(att)

    os.path.walk(os.path.realpath(file_path), add_file, ())


def main(mail, passwd, file_path):
    smtp = check_mail_service(mail)
    try:
        test = smtp.login(mail, passwd)
        msg = MIMEMultipart()
    except smtplib.SMTPException, e:
        print(e)


if __name__ == '__main__':
    mail = ''
    passwd = ''
    file_path = '/home/hidden/Downloads/子乌书简全站mobi书籍_part1'
    # main(mail, passwd, file_path)
    msg = MIMEMultipart()
    add_attach_p(msg, file_path)