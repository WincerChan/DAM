#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait
 
lock = threading.Lock()
class Downloader(): 
    def __init__(self, url):
        self.url = url
        self.num = 5
        self.name = self.url.split('/')[-1]
        r = requests.head(self.url)
        print(r.status_code)
        if r.status_code == 302:
            self.url = r.headers['Location']
            print("该url已重定向至{}".format(self.url))
            r = requests.head(self.url)
        self.size = int(r.headers['Content-Length'])
        print('该文件大小为：{} bytes'.format(self.size))

    def down(self, start, end):
        
        headers = {'Range': 'bytes={}-{}'.format(start, end)}
        r = requests.get(self.url, headers=headers, stream=True)

        # 写入文件对应位置
        lock.acquire()
        with open(self.name, "rb+") as fp:
            fp.seek(start)
            fp.write(r.content)
            lock.release()
        
 
    def run(self):
        #  创建一个和要下载文件一样大小的文件
        fp = open(self.name, "wb")
        fp.truncate(self.size)
        fp.close()
 
        # 启动多线程写文件
        part = self.size // self.num  
        pool = ThreadPoolExecutor(max_workers = self.num)
        futures = []
        for i in range(self.num):
            start = part * i
            if i == self.num - 1:   # 最后一块
                end = self.size
            else:
                end = start + part - 1
                print(start, end)
            futures.append(pool.submit(self.down, start, end))
        wait(futures)
        print('%s 下载完成' % self.name)
 
if __name__ == '__main__':
    url = ''
    start = time.time()  
    down = Downloader(url)
    down.run()
    end = time.time()
    print("用时: ", end='')
    print(end-start
