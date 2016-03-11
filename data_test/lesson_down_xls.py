# -- coding:utf8 -- #
import xlwt
import xlrd
import MySQLdb


def read_xxl(path_name):
    data = xlrd.open_workbook(path_name)
    table = data.sheets()[0]
    return (table.row_values(i)[0] for i in range(table.nrows) if table.row_values(i)[0])


def create_xsl(xml_name):
    workbook = xlwt.Workbook(encoding='ascii')
    sheet = workbook.add_sheet('test', cell_overwrite_ok=True)
    sheet.write(0, 0, u'课程')
    sheet.write(0, 1, u'章节')
    sheet.write(0, 2, u'下载地址')
    return workbook, sheet


def get_cur():
    con = MySQLdb.Connect(host='192.168.1.142', user='root', passwd='1234', port=3306, charset='utf8')
    cur = con.cursor()
    return con, cur


def get_course(cur, course_name):
    sql = '''select name, video_url from lps_20160307.mz_course_lesson where course_id in (select id from lps_20160307.mz_course_course where name="%s")'''
    try:
        cur.execute(sql % course_name)
    except Exception, e:
        print e
    data = cur.fetchall()
    return data


if __name__ == '__main__':
    con, cur = get_cur()
    r_path_name = '/home/hidden/Downloads/需要下载的课程列表.xlsx'
    w_path_name = '/home/hidden/Downloads/result.xls'
    workbook, sheet = create_xsl(w_path_name)
    line = 1
    li = read_xxl(r_path_name)
    for course_name in li:
        sheet.write(line, 0, course_name)
        line += 1
        data = get_course(cur, course_name)
        for i in data:
            sheet.write(line, 1, i[0])
            sheet.write(line, 2, i[1])
            line += 1
    workbook.save(w_path_name)
    cur.close()
    con.close()
