# -*- coding: utf-8 -*-
import urlib,urllib2
import requests
url = 'http://www.baidu.com'
url2 = urllib2.Request(url)     #使用urllib2的request方法发起请求
response = urllib2.urlopen(url2)  #用urlopen打开上一步返回的结果，得到请求后的响应内容
apicon = response.read()  #读取response
print(apicon)
