# py-downloader
A multi-threaded downloader written by python.

## Usage
python    test.py    \[\<url>]    \[-n <选项>]    [-o <选项>]

| 选项                 | 参数   | 含义           |
| :----------------- | :--- | :----------- |
| url                | None | 指定下载链接       |
| num-connection = x | -n x | 指定链接数目（即线程数） |
| outputfile=f       | -o f | 指定本地输出文件     |
| help               | -h   | 帮助信息         |
| version            | -v   | 版本信息         |

## Example

![](image/Example1.png)

## To Do

- Display real-time speed
- Add breakpoint continue feature
