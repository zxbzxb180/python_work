# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_test.models import *

class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TopicItem_1(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    create_time = scrapy.Field()
    answer_nums = scrapy.Field()
    click_nums = scrapy.Field()
    score = scrapy.Field()  # 赏分
    status = scrapy.Field()  # 状态
    last_answer_time = scrapy.Field()

    def save(self):
        topic = Topic()
        topic.id = self['id']
        topic.title = self['title']
        topic.author = self['author']
        topic.create_time = self['create_time']
        topic.answer_nums = self.get('answer_nums', 0)
        topic.click_nums = self.get('click_nums', 0)
        topic.score = self.get('score', 0)  # 赏分
        topic.status = self['status']  # 状态
        topic.last_answer_time = self['last_answer_time']

        existed_topics = Topic.select().where(Topic.id == topic.id)
        if existed_topics:
            topic.save()
        else:
            topic.save(force_insert=True)


class TopicItem_2(scrapy.Item):
    id = scrapy.Field()
    content = scrapy.Field()
    jtl = scrapy.Field()  # 结帖率
    praised_nums = scrapy.Field()  # 点赞数

    def save(self):
        existed_topics = Topic.select().where(Topic.id == self['id'])
        if existed_topics:
            topic = existed_topics[0]
            topic.content = self['content']
            topic.praised_nums = self.get('praised_nums', 0)
            topic.jtl = self.get('jtl', 0)
            topic.save()


class AnswerItem(scrapy.Item):
    topic_id = scrapy.Field()
    author = scrapy.Field()
    create_time = scrapy.Field()
    content = scrapy.Field()
    praised_nums = scrapy.Field()  # 点赞数

    def save(self):
        answer = Answer()
        answer.topic_id = self['topic_id']
        answer.author = self['author']
        answer.create_time = self['create_time']
        answer.content = self['content']
        answer.praised_nums = self['praised_nums']

        answer.save()


class AuthorItem(scrapy.Item):
    id = scrapy.Field()
    desc = scrapy.Field()
    following_nums = scrapy.Field()  # 关注数

    def save(self):
        author = Author()
        author.id = self['id']
        author.desc = self['desc']
        author.following_nums = self['following_nums']
        existed_author = Author.select().where(Author.id == self['id'])
        if existed_author:
            author.save()
        else:
            author.save(force_insert=True)


class AuthorBlogItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    click_nums = scrapy.Field()
    praised_nums = scrapy.Field()  # 点赞数
    original_nums = scrapy.Field()  # 原创数
    forward_nums = scrapy.Field()  # 转发数
    rate = scrapy.Field()  # 排名
    answer_nums = scrapy.Field()  # 评论数
    industry = scrapy.Field()  # 行业
    location = scrapy.Field()  # 地址
    follower_nums = scrapy.Field()  # 粉丝数

    def save(self):
        existed_author = Author.select().where(Author.id == self['id'])
        if existed_author:
            author = existed_author[0]
            author.original_nums = self.get('original_nums', 0)
            author.follower_nums = self.get('follower_nums', 0)
            author.praised_nums = self.get('praised_nums', 0)
            author.answer_nums = self.get('answer_nums', 0)
            author.click_nums = self.get('click_nums', 0)
            author.rate = self.get('rate', -1)
            author.name = self['name']
            author.save()