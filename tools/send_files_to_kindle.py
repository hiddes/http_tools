# -- coding:utf8 -- #
import smtplib
import socket
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import Queue
import time

__auto__ = u'俗子'

# 最大附件大小
MAX_SIZE = 1024 * 1024 * 48
MAX_NUM = 25

queue = Queue.Queue()


# tl = threading.Lock()


def check_mail_service(mail, server=0, ssl=0):
    port_list = [25, 465]
    # company mail list ,maybe add by end
    company_mail = [None, 'exmail.qq.com']
    server_name = mail.split('@')[1]
    try:
        if company_mail[server] is None:
            server_host = ''.join(('smtp.', server_name))
            smtp = smtplib.SMTP(server_host, port_list[ssl], timeout=5)
        else:
            server_host = ''.join(('smtp.', company_mail[server]))
            smtp = smtplib.SMTP(server_host, port_list[ssl], timeout=5)
    except (socket.timeout, socket.error):
        return check_mail_service(mail, server + 1)
    else:
        return smtp, server_host, port_list[ssl]


# 存储已发送数据
ok_dict = dict()


# 多线程
class AddAttach(threading.Thread):
    def __init__(self, smtp, from_mail, to_mail, **kwargs):
        threading.Thread.__init__(self)
        self.smtp = smtp
        # send ok data
        self.ok_list = list()
        # no send data
        self.bad_list = list()
        self.server_host = kwargs.get('server_host')
        self.server_port = kwargs.get('server_port')
        self.size_num = 0
        self.from_mail = from_mail
        self.to_mail = ';'.join(to_mail)
        self.subject = 'kindle file' if not kwargs.has_key('subject') else kwargs.get('subject')
        self.body = 'send to kindle files' if not kwargs.has_key('body') else kwargs.get('body')

    def run(self):
        msg = self.get_msg()
        while (not queue.empty()):
            file_name = queue.get(timeout=5)
            self.ok_list.append(file_name)
            self.size_num += os.path.getsize(file_name)
            # 先添加再判断
            if len(self.ok_list) > MAX_NUM or self.size_num > MAX_SIZE:
                if self.send_mail(msg):
                    print('send to ok list:', self.ok_list[:-1])
                    ok_dict.update({i: 'ok' for i in self.ok_list[:-1]})
                    self.ok_list = [file_name]
                else:
                    self.bad_list.append(self.ok_list[:-1])
                    self.ok_list = [file_name]
                self.size_num = os.path.getsize(file_name)
                msg = self.get_msg()
            self.add_attach(msg, file_name)
        print('send ok list:', ok_dict.keys())
        print('no send list:', self.bad_list)

    def get_msg(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['To'] = self.to_mail
        msg['From'] = self.from_mail
        msg.attach(MIMEText(self.body))
        return msg

    @staticmethod
    def add_attach(msg, f):
        att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = ''.join(('attachment; filename=', os.path.basename(f)))
        msg.attach(att)

    def send_mail(self, msg):
        try:
            time.sleep(3000)
            self.smtp.sendmail(self.from_mail, self.to_mail, msg.as_string())
            return True
        except smtplib.SMTPDataError, e:
            if 451 in e:
                print('文件大了')
            return False
        except smtplib.SMTPServerDisconnected:
            if self.server_port and self.server_host:
                self.smtp.connect(self.server_host, self.server_port)
            else:
                self.smtp.connect()
            self.send_mail(msg)
        except Exception, e:
            print(e)
            return False


def put_queue(file_path):
    assert os.path.isdir(file_path)

    def add_file(*fi):
        for i in fi[2]:
            file_name = ''.join((fi[1], os.path.sep, i))
            if not os.path.isdir(file_name):
                queue.put(file_name)

    os.path.walk(os.path.realpath(file_path), add_file, ())


# 多进程
def test_p(smtp, to_mail, from_mail, body, **kwargs):
    # sendto = kwargs.get('sendto')
    server_host = kwargs.get('server_host')
    server_port = kwargs.get('server_port')

    def add_attach(msg, f):
        att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = ''.join(('attachment; filename=', os.path.basename(f)))
        msg.attach(att)

    def get_msg():
        msg = MIMEMultipart()
        msg['Subject'] = 'test'
        msg['To'] = ";".join(to_mail)
        msg['From'] = from_mail
        msg.attach(MIMEText(body))
        return msg

    def send_mail(msg):
        try:
            time.sleep(3)
            smtp.sendmail(from_mail, to_mail, msg.as_string())
            return True
        except smtplib.SMTPDataError, e:
            if 451 in e:
                print('文件大了')
            return False
        except smtplib.SMTPServerDisconnected:
            if server_host and server_port:
                smtp.connect(server_host, server_port)
            else:
                smtp.connect()
            send_mail(msg)
        except Exception, e:
            print(e)
            return False

    msg = get_msg()
    ok_list = list()
    bad_list = list()
    size_num = 0

    while (not queue.empty()):
        file_name = queue.get(timeout=5)
        ok_list.append(file_name)
        file_size = os.path.getsize(file_name)
        if file_size > MAX_SIZE:
            continue
        size_num += file_size
        # 先添加再判断
        if len(ok_list) > MAX_NUM or size_num > MAX_SIZE:
            if send_mail(msg):
                print('send to ok list:', ok_list[:-1])
                ok_dict.update({i: 'ok' for i in ok_list[:-1]})
                ok_list = [file_name]
            else:
                bad_list.append(ok_list[:-1])
                ok_list = [file_name]
            size_num = file_size
            msg = get_msg()
        add_attach(msg, file_name)
    print('send ok list:', ok_dict.keys())
    print('no send list:', bad_list)


def main(mail, passwd, file_path, sendto):
    smtp, server_host, server_port = check_mail_service(mail)
    try:
        put_queue(file_path)
        test_ = smtp.login(mail, passwd)
        if 'successful' in test_[1]:
            print('login ok!!!')
            test_p(smtp, send_to, mail, 'test', server_host=server_host, server_port=server_port)

            # 多线程启动
            # thread_list = list()
            # thread_num = 5
            # for i in xrange(thread_num):
            #     thread_list.insert(0, AddAttach(smtp, mail, send_to, server_host=server_host, server_port=server_port))
            #     thread_list[0].start()
            #     print('start job...', i)
    except smtplib.SMTPException, e:
        print(e)
    except Exception, e:
        print(e)


if __name__ == '__main__':
    mail = 'test@maiziedu.com'
    passwd = 'test.'
    send_to = ['test@kindle.cn', ]
    file_path = '/home/hidden/Downloads/子乌书简全站mobi书籍_part1'
    main(mail, passwd, file_path, send_to)
    # msg = MIMEMultipart()
    # add_attach_p(msg, file_path)
