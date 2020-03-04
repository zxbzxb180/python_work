from peewee import *

# 数据库名、 IP地址、 端口号、 用户名、 密码
db = MySQLDatabase('temperature', host='127.0.0.1', port=3306, user='root', password='123456')


class Temperature(Model):
    date = CharField(max_length=20, null=True)
    time = CharField(max_length=20, null=True)
    temperature = CharField(max_length=20, null=True)
    humidity = CharField(max_length=20, null=True)

    class Meta:
        database = db
        table_name = 'shenzhen'


class Temperature2(Model):
    date = CharField(max_length=20, null=True)
    time = CharField(max_length=20, null=True)
    temperature = CharField(max_length=20, null=True)
    humidity = CharField(max_length=20, null=True)

    class Meta:
        database = db
        table_name = 'guangzhou'


class Temperature3(Model):
    date = CharField(max_length=20, null=True)
    time = CharField(max_length=20, null=True)
    temperature = CharField(max_length=20, null=True)
    humidity = CharField(max_length=20, null=True)

    class Meta:
        database = db
        table_name = 'foshan'


class Temperature4(Model):
    date = CharField(max_length=20, null=True)
    time = CharField(max_length=20, null=True)
    temperature = CharField(max_length=20, null=True)
    humidity = CharField(max_length=20, null=True)

    class Meta:
        database = db
        table_name = 'dongguan'


if __name__ == '__main__':
    db.create_tables([Temperature, Temperature2, Temperature3, Temperature4])

