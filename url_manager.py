class UrlManager(object):
	"""docstring for UrlManager"""
	def __init__(self):
		self.new_urls = set()
		self.older_urls = set()

	def add_new_url(self, url):
		print 'add new url'

		if url is None:
			print 'url is none'
			return

		if url not in self.new_urls and url not in self.older_urls:
			self.new_urls.add(url)

	def add_new_urls(self, urls):
		if urls is None or len(urls)==0:
			return

		for url in urls:
			self.add_new_url(url)

	def has_new_url(self):
		return len(self.new_urls)!=0

	def get_new_url(self):
		print 'get_new_url size ', len(self.new_urls)

		new_url = self.new_urls.pop()
		print 'new_url, size', new_url, len(self.new_urls)

		self.older_urls.add(new_url)
		
		print 'get_new_url ', new_url

		return new_url