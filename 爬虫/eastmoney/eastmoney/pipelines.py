# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class EastmoneyPipeline(object):
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
            db='eastmoney',
            # 编码格式
            charset='utf8',
            use_unicode=True)

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = 'insert into `asia_money`(`序号`,`名称`,`最新价`,`涨跌额`,`涨跌幅`,`开盘价`,`最高价`,`最低价`,`昨收价`,`振幅`,`最新行情时间`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (
        item['number'], item['name'], item['latest_price'], item['amount_of_rise_and_fall'], item['rate_of_rise_and_fall'], item['today_opening_price'], item['maximum_price'], item['minimum_price'], item['yesterday_closing_price'], item['amplitude'], item['update_time'])
        value = (item['number'])
        self.cursor.execute(insert_sql,values)
        self.conn.commit()
        return item
