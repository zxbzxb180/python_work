# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

import pymysql.cursors

class DoubanPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            # localhost连接的是本地数据库
            host='localhost',
            # mysql数据库的端口号
            port=3306,
            # 数据库的用户名
            user='root',
            # 本地数据库密码
            passwd='123456',
            # 表名
            db='douban',
            # 编码格式
            charset='utf8',
            use_unicode=True)

        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        insert_sql = 'insert into `movie_list`(`serial_number`,`movie_name`,`introduce`,`star`,`evaluate`,`describe`) values(%s,%s,%s,%s,%s,%s)'
        values = (item['serial_number'], item['movie_name'], item['introduce'], item['star'], item['evaluate'], item['describe'])
        self.cursor.execute(insert_sql, values)
        self.conn.commit()
        return item



