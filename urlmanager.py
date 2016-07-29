#encoding utf8

import urllib2, cookielib

url = 'http://www.baidu.com'
response = urllib2.urlopen(url)
print response.getcode()

#metho2
request = urllib2.Request(url)

#add add
#request.add_data('a','1')

#add header
request.add_header('User-Agent','Mozilla/5.0')

response = urllib2.urlopen(request)

print response.getcode()

#method3
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen(url)

print response.read()

