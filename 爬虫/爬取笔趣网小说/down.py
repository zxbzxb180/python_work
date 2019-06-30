#coding=gbk
		
from bs4 import BeautifulSoup
import requests
import sys


class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []            #����½���
        self.urls = []            #����½�����
        self.nums = 0            #�½���


    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,"html.parser")
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),"html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a[16:])                                #�޳�����Ҫ���½ڣ���ͳ���½��� 
        for each in a[16:]: 
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

 
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.find_all('div', class_ = 'showtxt')		
        texts = texts[0].text.replace('\xa0'*8,'\n\n')        
        return texts


    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('��һ�����㡷��ʼ���أ�')
    
    for i in range(dl.nums):
        try:
            dl.writer(dl.names[i],'һ������1.txt',str(dl.get_contents(dl.urls[i])))
        except:
            print("failed!")			                      
        '''sys.stdout.write("������:%.3f%%" %float(i/dl.nums) + '\r')
        sys.stdout.flush()'''
        print("\r������:%.3f%%" % float(i / dl.nums), end="")
    print('��һ�����㡷�������')
