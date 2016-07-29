#coding:utf8

from pprint import pprint
from time import time
import logging

class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return

		self.datas.append(data)

	def output_html(self):
		fout = open('output.html','w')

		fout.write("<html>")
		fout.write("<meta charset='utf-8'>")
		fout.write("<head>")
		fout.write("</head>")

		fout.write("<body>")

		fout.write("<table>")
		for data in self.datas:
			try:
				fout.write("<tr>")
				fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
				fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
				fout.write("</tr>")
			except:
				print 'fail to output title or summary'

		fout.write("</table>")

		fout.write("</body>")

		fout.write("</html>")
		fout.close()