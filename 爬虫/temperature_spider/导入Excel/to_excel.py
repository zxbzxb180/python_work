import pymysql
import xlwt


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='temperature', charset='utf8')
    return conn


def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()


def add(workbook, place):
    list_table_head = ['日期', '时间', '温度', '相对湿度']
    sheet = workbook.add_sheet(place, cell_overwrite_ok=True)
    for i in range(len(list_table_head)):
        sheet.write(0, i, list_table_head[i])

    conn = get_conn()
    cur = conn.cursor()
    sql = 'select * from `{}`'.format(place)
    results = query_all(cur, sql, None)
    conn.commit()
    cur.close()
    conn.close()
    row = 1
    for result in results:
        col = 0
        print(type(result))
        print(result)
        i = 0
        for item in result:
            if i == 0:
                i += 1
            else:
                print(item)
                sheet.write(row, col, item)
                col += 1
        row += 1


if __name__ == '__main__':
    list_table_head = ['日期', '时间', '温度', '相对湿度']
    workbook = xlwt.Workbook()
    add(workbook, 'shenzhen')
    add(workbook, 'guangzhou')
    add(workbook, 'foshan')
    add(workbook, 'dongguan')

    from datetime import datetime
    workbook.save('{}.xlsx'.format(datetime.now().strftime("%Y-%m-%d")))