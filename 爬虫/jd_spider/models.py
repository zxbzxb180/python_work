from peewee import *

db = MySQLDatabase('jd_good', host='127.0.0.1', port=3306, user='root', password='123456')


class BaseModel(Model):
    class Meta:
        database = db


class Good(BaseModel):
    id = BigIntegerField(primary_key=True, verbose_name='商品id')
    name = CharField(max_length=500, verbose_name='商品名称')
    price = FloatField(default=0.0, verbose_name='商品价格')
    content = TextField(default='', verbose_name='商品内容')
    supplier = CharField(default='', verbose_name='商品来源')
    ggbz = CharField(default='', verbose_name='规格和包装')
    image_list = TextField(default='', verbose_name='商品轮播图')

    good_rate = IntegerField(default=0, verbose_name='好评率')
    evaluate_nums = IntegerField(default=0, verbose_name='评价数')
    has_image_evaluate_nums = IntegerField(default=0, verbose_name='晒图数')
    has_video_evaluate_nums = IntegerField(default=0, verbose_name='视频晒单数')
    has_add_evaluate_nums = IntegerField(default=0, verbose_name='追评数')
    well_evaluate_nums = IntegerField(default=0, verbose_name='好评数')
    middle_evaluate_nums = IntegerField(default=0, verbose_name='中评数')
    bad_evaluate_nums = IntegerField(default=0, verbose_name='差评数')


class GoodEvaluate(BaseModel):
    id = CharField(primary_key=True)
    good = ForeignKeyField(Good, verbose_name='商品')
    user_head_url = CharField(verbose_name='用户头像')
    user_name = CharField(verbose_name='用户名')
    good_info = CharField(default='', max_length=500, verbose_name='商品信息')
    evaluate_time = DateTimeField(verbose_name='评价时间')
    content = TextField(default='', verbose_name='评价内容')
    star = IntegerField(default=0, verbose_name='评分')
    comment_nums = IntegerField(default=0, verbose_name='评论数')
    praised_nums = IntegerField(default=0, verbose_name='点赞数')
    image_list = TextField(default='', verbose_name='图片')
    video_list = TextField(default='', verbose_name='视频')


class GoodEvaluateSummary(BaseModel):
    good = ForeignKeyField(Good, verbose_name='商品')
    tag = CharField(max_length=20, verbose_name='标签')
    num = IntegerField(default=0, verbose_name='数量')


if __name__ == '__main__':
    db.create_tables([Good, GoodEvaluate, GoodEvaluateSummary])