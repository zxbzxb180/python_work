#coding=gbk
import requests
from bs4 import BeautifulSoup
import sys

class downloader(object):
    #��ȡ��������
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/book/2337/'
        self.names = [] #����½�����
        self.urls = []#����½�����
        self.nums = 0 #�½���

    """
       ����˵��:��ȡ��������
       Parameters:
           ��
       Returns:
           ��
       Modify:
           2017-09-13
       """

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text

        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all('div', class_='book_list')

        a_bf = BeautifulSoup(str(div[0]), "html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a[16:])
        #ɾ����������½�
        for each in a[16:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
        ����˵��:��ȡ�½�����
        Parameters:
            target - ��������(string)
        Returns:
            texts - �½�����(string)
        Modify:
            2017-09-13
        """

    def get_contents(self,target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.find_all('div',class_='book_list')
        texts = texts[0].text.replace('\xa0'*4,'\n\n')
        return texts

    """
       ����˵��:����ȡ����������д���ļ�
       Parameters:
           name - �½�����(string)
           path - ��ǰ·����,С˵��������(string)
           text - �½�����(string)
       Returns:
           ��
       Modify:
           2017-09-13
       """
    def writer(self,name,path,text):
        write_flag  = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('��ç�ļ͡���ʼ����')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'ç�ļ�.txt',dl.get_contents(dl.urls[i]))
        sys.stdout.write("������:%.3f%%" % float(i/dl.nums) + '\r')

        sys.stdout.flush()
        print('�������')

