from peewee import *

db = MySQLDatabase('csdn_bbs', host='127.0.0.1', port=3306, user='root', password='123456')


class BaseModel(Model):
    class Meta:
        database = db
        table_name = 'users'


class Topic(BaseModel):
    id = IntegerField(primary_key=True)
    title = CharField()
    content = TextField(default='')
    author = CharField()
    create_time = DateTimeField()
    answer_nums = IntegerField(default=0)
    click_nums = IntegerField(default=0)
    praised_nums = IntegerField(default=0)  # 点赞数
    jtl = FloatField(default=0.0)  # 结帖率
    score = IntegerField(default=0)  # 赏分
    status = CharField()  # 状态
    last_answer_time = DateTimeField()


class Answer(BaseModel):
    topic_id = IntegerField()
    author = CharField()
    create_time = DateTimeField()
    content = TextField(default='')
    praised_nums = IntegerField(default=0)  # 点赞数


class Author(BaseModel):
    id = CharField(primary_key=True)
    name = CharField()
    click_nums = IntegerField(default=0)
    praised_nums = IntegerField(default=0)  # 点赞数
    original_nums = IntegerField(default=0)  # 原创数
    forward_nums = IntegerField(default=0)  # 转发数
    rate = IntegerField(default=-1)  # 排名
    answer_nums = IntegerField(default=0)  # 评论数
    desc = TextField(null=True)
    industry = CharField(null=True)  # 行业
    location = CharField(null=True)  # 地址
    follower_nums = IntegerField(default=0)  # 粉丝数
    following_nums = IntegerField(default=0)  # 关注数


if __name__ == '__main__':
    db.create_tables([Topic, Answer, Author])