2016.07.27

爬虫介绍
简单的爬虫架构
url管理器
网页下载器
网页解析器beautiful soap
完整实例

爬虫是什么？

爬虫的价值
互联网数据，可以更好的使用

基于数据，做出更好的产品
提供新闻阅读器
最爆笑故事的app
最漂亮的美女图片网站
图书价格对比网站
python技术文章大全（整合）

简单的爬虫架构
1. 爬虫的调度端：爬虫（url管理器：取出一个待爬取的url，网页下载器、网页解析器）－－产生有价值的数据，另外每个网页有其他URL，补充进url管理器；循环过程，只要有关联的url，就会一直运行下去；
2. 运行流程；调度器（从URL管理器取出一个Url，如果是有效的，则调用下载器下载，获得内容，同时调用分析器进行分析，获得内容和新的url，内容存放，url添加到url管理器；

url管理器：管理待抓取的URL集合，已抓取的url集合，
防止重复抓取和循环抓取

url管理器实现方式，存取在内存中，（待爬取 set（）， 已爬取set（））去取重复元素
关系数据库：mysql等， table_urls（url，is_crawled）
缓存数据库zhong：redis（ 待爬取set，已爬取set）

网页下载器
将互联网上的url对应的网页下载到本地的工具
urllib2，python官方基础模块，可以支持登录网页的cookie，代理功能
request，第三方包更强大

urllib2的三个下载网页方法
import urllib2
response = urllib2.urlopen('http://www.baidu.com')
//判断是否200
print response.getcode()

#读取内容
cont = response.read()

urllib2下载网页方法2， 添加打他， http header
url，data, header
urllib2.Request
urllib2.urlopen(request)
import urllib2
#创建request对象
request = urllib2.Request(url)
#添加数据
request.add_data('a','1')
＃添加http header
request.add_header('User-agent','')

安装sublime text3的代码补插件

网页解析器
从网页中提取有价值数据的工具

python有几种网页解析器
正则表达式，使用模糊匹配，字符串匹配

其他都是结构化解析：
html.parser
beautiful soup(第三方插件)
lxml

网页解析器
结构化解析－DOM（document object model）树
遍历和访问
document, html, header, body, title, p

beautiful soup
pyhton第三方库，用于从html中提取数据

安装pip install beautifulsoup4
import bs4

sudo easy_install pip
pip install beautifulsoup4

网页解析器－beautiful soup 语法
html网页－创建beautifulsoup对象－搜索节点（find_all，find），访问节点（名称、属性、文字）
	
<a href="123.html" class='article' >link</a>

lession15
实例爬虫
确定目标、分析目标、编写代码、执行爬虫
数据格式：分析标题和简介
网页编码：需要指定网页编码

安装html_parser
pip install html_parser

python如何打印log，包括当前文件，函数，行号
http://blog.csdn.net/zengbo1019/article/details/8694144

import sys

print sys._getframe().f_code.co_name
print sys._getframe().f_code.co_filename
print sys._getframe().f_code.co_lineno

独立文件common.py



