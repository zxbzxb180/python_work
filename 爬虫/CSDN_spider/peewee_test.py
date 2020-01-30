from peewee import *

db = MySQLDatabase('csdn_bbs', host='127.0.0.1', port=3306, user='root', password='123456')


class People(Model):
    name = CharField(max_length=20, null=True)
    birthday = DateField()

    class Meta:
        database = db
        table_name = 'users'


if __name__ == '__main__':
    # db.create_tables([People])
    from datetime import date

    # user = People(name='chenxi', birthday=date(1998, 7, 26))
    # user.save()
    #
    # user = People(name='chenxixi', birthday=date(1998, 9, 16))
    # user.save()

    # chenxi = People.select().where(People.name == 'chenxixia')

    chenxi = People.get(People.name == 'chenxixi')
    print(chenxi.birthday)