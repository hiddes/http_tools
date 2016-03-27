# -- coding:utf8 -- #
"""
解决linux zip解压乱码问题
"""

import os
import sys
import zipfile

__auto__ = u'俗子'


def check_encode(name, index=0):
    """
    check name'endoce and decode
    :param name:
    :param index:
    :return: decode's text
    """
    # 支持的编码格式
    decode_list = ['utf8', 'gbk', 'cp1252', 'cp936', 'cp932', 'gb2312']
    try:
        return name.decode(decode_list[index])
    except UnicodeDecodeError:
        return check_encode(name, index + 1)
    except IndexError:
        raise Exception('dot discern you str')
    except Exception, e:
        print e
        return name


def un_zip(zip_file):
    files = zipfile.ZipFile(zip_file, 'r')
    for f in files.namelist():
        f_name = check_encode(f)
        # pf = ''.join((os.path.dirname(zip_file), os.path.sep, os.path.dirname(f_name)))
        f_name = ''.join((os.path.dirname(zip_file), os.path.sep, f_name))
        pf = os.path.dirname(f_name)
        if not os.path.exists(pf) and pf != "":
            os.mkdir(pf)
        data = files.read(f)
        # 直接覆盖
        if not os.path.isdir(f_name):
            fo = open(f_name, 'w')
            fo.write(data)
            fo.close()
    files.close()


def un_zips():
    if len(sys.argv) < 2:
        print('place input two or to many prams!!!')
        exit(-1)
    file_paths = sys.argv[1:]
    for file_path in file_paths:
        un_zip(file_path)


if __name__ == '__main__':
    # file_path = '/home/hidden/Downloads/ziwu2.zip'
    # un_zip(file_path)
    un_zips()
