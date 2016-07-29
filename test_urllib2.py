#coding:utf-8
import urllib2, cookielib
import bs4

url = "http://www.baidu.com"

print 'first method'

response1 = urllib2.urlopen(url)
print 'code',response1.getcode()
print len(response1.read())


print 'second method'
request = urllib2.Request(url)
#request.add_data()
request.add_header('User_agent',"Mozzila/5.0")
response2 = urllib2.urlopen(request)
print 'code', response2.getcode()
print 'len', len(response2.read())

print 'third method'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print 'code', response3.getcode()
print 'len', len(response3.read())


