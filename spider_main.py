#coding:utf8

#爬虫总调用

import url_manager, html_downloader, html_parser, html_output
import sys
import common

class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_output.HtmlOutputer()

	def crawl(self,root_url):
		"""get one url
		// start to downloader
		// parse html
		"""

		common.get_cur_info(self)

		print 'start crawl'
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			new_url = self.urls.get_new_url()
			print 'new_url', new_url

			html_cont = self.downloader.download(new_url)
			new_urls, new_data = self.parser.parse(new_url, html_cont)
			self.urls.add_new_urls(new_urls)
			self.outputer.collect_data(new_data)	
			self.outputer.output_html()



	# def get_cur_info(self):
	# 	print sys._getframe().f_code.co_filename
	# 	print sys._getframe().f_code.co_name
	# 	print sys._getframe().f_lineno

if __name__ == '__main__':
	root_url = "http://baike.baidu.com/view/21087.htm"
	obj_spider = SpiderMain()
	obj_spider.crawl(root_url)


