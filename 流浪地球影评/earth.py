import csv
import re

import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud# 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
import copy


def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = [line.strip() for line in open('stoplist.txt',encoding='UTF-8').readlines()]
    # 输出结果为outstr
    outstr = []
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr.append(word)

    return outstr

def first():
    p = re.compile(r'[,.?!，。！？、；;:0-9：《》…“” +Mike\r\n★☆B（）()]')
    all_word_str = ''
    for i in list_1:
        subs = re.split(p, i[1])
        i[1] = ''.join(subs)
        all_word_str += i[1]

    all_word = seg_depart(all_word_str)

    word_counts = collections.Counter(all_word) # 词频统计

    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
        max_words=100, # 最多显示词数
        max_font_size=500,# 字体最大值
        background_color="white",
        width=1000,
        height=880,
    )

    wc.generate_from_frequencies(word_counts) # 从字典生成词云
    plt.imshow(wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像


def second():
    score_counts = collections.Counter(score_l)
    score_wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
        max_words=5, # 最多显示词数
        max_font_size=1200,# 字体最大值
        background_color="white",
        width=1000,
        height=880,
    )

    score_wc.generate_from_frequencies(score_counts) # 从字典生成词云
    plt.imshow(score_wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像

def third():
    p = re.compile(r'[,.?!，。！？、；;:0-9：《》…“” +Mike\r\n★☆B（）()]')
    good_content = ''
    for i in list_2:
        subs = re.split(p, i[1])
        i[1] = ''.join(subs)
        if i[5] in ["['50']", "['40']", "['30']"]:
            good_content += i[1]
        else:
            continue
    all_good_content = seg_depart(good_content)

    good_content_counts = collections.Counter(all_good_content)  # 词频统计

    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        max_words=100,  # 最多显示词数
        max_font_size=500,  # 字体最大值
        background_color="white",
        width=1000,
        height=880,
    )

    wc.generate_from_frequencies(good_content_counts)  # 从字典生成词云
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.show()  # 显示图像

def fouth():
    p = re.compile(r'[,.?!，。！？、；;:0-9：《》…“” +Mike\r\n★☆B（）()]')
    bad_content = ''
    for i in list_2:
        subs = re.split(p, i[1])
        i[1] = ''.join(subs)
        if i[5] in ["['20']", "['10']"]:
            bad_content += i[1]
        else:
            continue
    all_bad_content = seg_depart(bad_content)

    bad_content_counts = collections.Counter(all_bad_content)  # 词频统计

    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        max_words=100,  # 最多显示词数
        max_font_size=500,  # 字体最大值
        background_color="white",
        width=1000,
        height=880,
    )

    wc.generate_from_frequencies(bad_content_counts)  # 从字典生成词云
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.show()  # 显示图像

def sample_class_show(y):
    '''
    绘制饼图,其中y是标签列表
    '''
    target_stats=collections.Counter(y)
    labels = list(target_stats.keys())
    sizes = list(target_stats.values())
    explode = tuple([0.1] * len(target_stats))
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, shadow=True, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    csv_file = csv.reader(open('流浪地球.csv', 'r', encoding='utf-8'))

    list_1 = []  # 保存所有数据

    for line in csv_file:
        list_1.append(line)

    # 另外保存一次所有数据
    list_2 = copy.deepcopy(list_1)

    # 保存用户城市（citys）和评分（scores）两列[ ]里面的数据。
    l = []
    score_l = []
    for i in list_1:
        rule = r"\['(.*?)'\]"
        a = re.findall(rule, i[0])
        b = re.findall(rule, i[5])
        try:
            l.append([a[0], b[0]])
            score_l.append(b[0])
        except IndexError:

            if a is None and b is None:
                l.append(['', ''])
                score_l.append('')
            elif a is None and b is not None:
                l.append(['', b[0]])
                score_l.append(b[0])
            elif a is not None and b is None:
                l.append([a[0], ''])
                score_l.append('')

    l[0][0], l[0][1] = 'citys', 'scores'
    print(score_l)

    first()
    second()
    third()
    fouth()
    sample_class_show(score_l)

