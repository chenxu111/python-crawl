#coding:utf8

import urllib2
class HtmlDownloader(object):

	def download(self, url):
		print 'download url ', url
		if url is None:
			return

		response = urllib2.urlopen(url)
		code = response.getcode()

		if(code != 200):
			return
			
		content = response.read()
		# print content
		return content


