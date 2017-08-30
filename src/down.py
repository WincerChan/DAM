#!/usr/bin/env python
from getopt import GetoptError, getopt
from sys import argv, exit
from time import time

from Demo import Downloader


usage = """
用法： python test.py [<地址>] [-n <选项>] [-o <选项>]

url                      None     指定下载链接
num-connection=x         -n x     指定连接数目（即线程数）
outputfile=f             -o f     指定输出本地文件
help                     -h       帮助信息
version                  -v       版本信息

"""
version = """
版本 1.1 (Linux)

Copyright 2017 Wincer

详细信息阅读 CREDITS 文件

"""


def main(argv):
    try:
        if argv[0] not in ('-v', '-h'):
            inputurl = argv[0]
            argv = argv[1:]
        else:
            inputurl = ''
        numthread = ''
        outputfile = ''
        opts, args = getopt(argv, "hvn:o:")
    except GetoptError:
        print(usage)
        exit(2)
    except IndexError:
        print(usage)
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            exit()
        elif opt == '-v':
            print(version)
            exit()
        elif opt == "-n":
            numthread = arg
        elif opt == "-o":
            outputfile = arg
    print('输入的url为：{}'.format(inputurl))
    print('下载的线程数：{}'.format(numthread))
    print('输出的文件名为：{}'.format(outputfile))
    return inputurl, numthread, outputfile


if __name__ == "__main__":
    url, nums, file = main(argv[1:])
    start = time()
    if nums == '':
        # 若用户没有输入进程数，则设置默认进程数4
        nums = 4
    if file == '':
        # 若用户没有输入文件名，则产生随机文件名
        file = 'File' + str(int(time() % 10))
    try:
        down = Downloader(url, int(nums), file)
        down.run()
    except Exception as e:
        print(e)
        exit(2)
    end = time()
    print("用时: ", end='')
    print(end - start)
