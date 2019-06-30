#coding=gbk
		
from bs4 import BeautifulSoup
import requests, sys

class downloader(object):

    def __init__(self):
        self.server = 'http://www.17k.com'
        self.target = 'http://www.17k.com/list/2942984.html'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数


    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,"html.parser")
        div = div_bf.find_all('div', class_ = 'Volume')
        a_bf = BeautifulSoup(str(div[0]),"html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a)                                #剔除不必要的章节，并统计章节数 
        for each in a: 
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

 
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.find_all('div', class_ = 'pt')
		
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
    print('《最强赘婿》开始下载：')
    a=0
    for i in range(dl.nums):       
        dl.writer(dl.names[i], '最强赘婿.txt', str(dl.get_contents(dl.urls[i])))
        a=a+1
        print(a)
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《最强赘婿》下载完成')
