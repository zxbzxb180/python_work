from scrapy import Selector
import requests
from item import Temperature, Temperature2, Temperature3, Temperature4
import schedule
import time


def spider(url, place):
    text = requests.get(url).content.decode("utf-8")
    sel = Selector(text=text)

    date_all = sel.xpath('//div[@id="forecast"]/div[@class="detail"]')
    day_id = 0
    for date_item in date_all:
        if day_id <= 2:
            date_i = "".join(date_item.xpath('.//div[@class="today"]/table/tbody/tr[1]/td[2]/text()').extract()).strip()
        else:
            date_i = "".join(date_item.xpath('.//div[@class="today"]/table/tbody/tr[1]/td[1]/text()').extract()).strip()
        time_all = sel.xpath('//div[@id="hour3"]/div')
        time_item = time_all[day_id]
        for item in range(0, 8):
            time_i = "".join((time_item.xpath('.//div[@class="row first"]/div/text()'))[item+1].extract()).strip()
            temperature = "".join((time_item.xpath('.//div[@class="row wd"]/div/text()'))[item+1].extract()).strip()
            humidity = "".join((time_item.xpath('.//div[@class="row xdsd"]/div/text()'))[item+1].extract()).strip()

            if place == 'shenzhen':
                existed_data = Temperature.select().where((Temperature.date == date_i)&(Temperature.time == time_i))
                if existed_data:
                    temperature_data = existed_data[0]
                else:
                    temperature_data = Temperature()
            elif place == 'guangzhou':
                existed_data = Temperature2.select().where((Temperature2.date == date_i)&(Temperature2.time == time_i))
                if existed_data:
                    temperature_data = existed_data[0]
                else:
                    temperature_data = Temperature2()
            elif place == 'foshan':
                existed_data = Temperature3.select().where((Temperature3.date == date_i)&(Temperature3.time == time_i))
                if existed_data:
                    temperature_data = existed_data[0]
                else:
                    temperature_data = Temperature3()
            elif place == 'dongguan':
                existed_data = Temperature4.select().where((Temperature4.date == date_i)&(Temperature4.time == time_i))
                if existed_data:
                    temperature_data = existed_data[0]
                else:
                    temperature_data = Temperature4()

            temperature_data.date = date_i
            temperature_data.time = time_i
            temperature_data.temperature = temperature
            temperature_data.humidity = humidity

            temperature_data.save()

        day_id += 1


def task1():
    spider(shenzhen_url, 'shenzhen')


def task2():
    spider(guangzhou_url, 'guangzhou')


def task3():
    spider(foshan_url, 'foshan')


def task4():
    spider(dongguan_url, 'dongguan')


def run():
    # schedule.every().day.at("18:43").do(task1)  # 每天的18:43分
    # schedule.every().day.at("18:43").do(task2)
    # schedule.every().day.at("18:43").do(task3)
    # schedule.every().day.at("18:43").do(task4)

    # schedule.every().hour.do(task1)  # 每个小时
    # schedule.every().hour.do(task2)
    # schedule.every().hour.do(task3)
    # schedule.every().hour.do(task4)

    schedule.every().minute.at(":00").do(task1)  # 每一个整点
    schedule.every().minute.at(":00").do(task2)
    schedule.every().minute.at(":00").do(task3)
    schedule.every().minute.at(":00").do(task4)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    shenzhen_url = 'http://www.nmc.cn/publish/forecast/AGD/shenzhen.html'
    guangzhou_url = 'http://www.nmc.cn/publish/forecast/AGD/guangzhou.html'
    foshan_url = 'http://www.nmc.cn/publish/forecast/AGD/foshan.html'
    dongguan_url = 'http://www.nmc.cn/publish/forecast/AGD/dongguan.html'

    run()
