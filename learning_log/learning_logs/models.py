#coding=gbk
from django.db import models


# Create your models here.
class Topic(models.Model):
    """�û�ѧϰ������"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """����ģ�͵��ַ�����ʾ"""
        return self.text


class Entry(models.Model):
    """ѧ�����й�ĳ������ľ���֪ʶ"""

    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """����ģ�͵��ַ�����ʾ"""
        return self.text[:50]+"..."