#coding:utf8

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
	"""docstring for HtmlParser"""

	def parse(self, page_url, html_cont):
		print 'parse'
		if page_url is None:
			print 'page_url is none'
			return

		if html_cont is None:
			print 'html_cont is none'			
			return

		soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')

		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)

		return new_urls, new_data

	def _get_new_urls(self, page_url, soup):
		print 'get_new_urls'
		new_urls = set()

		links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
		for link in links:
			new_url = link['href']
			print "find more links:" , new_url
			new_full_url = urlparse.urljoin(page_url, new_url)
			print "find more full links:" , new_full_url
			new_urls.add(new_full_url)
			print len(new_urls)

		return new_urls

	def _get_new_data(self, page_url, soup):
		print '_get_new_data'
		res_data = {}
		
		try:
			title_node = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
			res_data['title'] = title_node.get_text()
			print 'title: ', res_data['title']

			summary_node = soup.find('div', class_="lemma-summary")
			res_data['summary'] = summary_node.get_text()

			print 'summary ', res_data['summary']

		except:
			print 'parse failed'

		return res_data
