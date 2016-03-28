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
    except Exception:
        # 转不了，就算了吧    经测试，不影响使用
        return name


def un_zip(zip_file):
    """
    执行解压行为的过程
    :param zip_file:
    :return:
    """
    files = zipfile.ZipFile(zip_file, 'r')
    for f in files.namelist():
        # 解决乱码，就这儿拉
        f_name = check_encode(f)
        # 绝对路径，比较保险
        f_name = ''.join((os.path.dirname(zip_file), os.path.sep, f_name))
        # 父目录
        pf = os.path.dirname(f_name)
        if not os.path.exists(pf) and pf != "":
            # 创建父目录
            os.mkdir(pf)
        data = files.read(f)
        # 不是目录直接覆盖
        if not os.path.isdir(f_name):
            fo = open(f_name, 'w')
            fo.write(data)
            fo.close()
    files.close()


def un_zips():
    """
    批量处理，接受命令行 多个文件
    :return:
    """
    if len(sys.argv) < 2:
        print('place input two or to many prams!!!')
        exit(-1)
    file_paths = sys.argv[1:]
    for file_path in file_paths:
        # 解压
        un_zip(os.path.realpath(file_path))


if __name__ == '__main__':
    # file_path = '/home/hidden/Downloads/ziwu2.zip'
    # un_zip(file_path)
    un_zips()
