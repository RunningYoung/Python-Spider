# -*- coding: utf-8 -*-

# 导入re模板 正则表达式
import re

# import urllib2
# import urllib
# import cookielib

# # GET 请求
# values = {}
# values['username'] = "liangliang103377"
# values['password'] = "ASDF7431113"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# url = url + "?" + data
# print url
# request = urllib2.Request(url)
# respone = urllib2.urlopen(request)
# print respone.read()

# # POST 请求
# values = {}
# values['username'] = "liangliang103377"
# values['password'] = "ASDF7431113"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# request = urllib2.Request(url)
# respone = urllib2.urlopen(request)
# print respone.read()

# # URLError

# request = urllib2.Request('http://www.xxxxx.com')
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError, e:
#     print e.reason

# # HTTPError 和 URLError 混合使用
# req = urllib2.Request('http://blog.csdn.net/cqcre')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     if hasattr(e, "code"):
#         print e.code
#     if hasattr(e, "reason"):
#         print e.reason
# except urllib2.URLError, e:
#     if hasattr(e, "reason"):
#         print e.reason
# else:
#     print 'OK'

# # cookielib的使用
# # 声明一个CookieJar 对象实例来保存cookie
# cookie = cookielib.CookieJar()
# # 利用urllib2库的HTTPCookirProcessor对象来创建cookie处理
# handle = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handle)
# # 此处的open方法同urllib2的urlopen方法，也可以传入request
# respones = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value
#     print item
# # print respones.read()

# *******************保存cookie到文件**************
# # 设置保存Cookie的文件，同级目录下的cookie.tx
# fileName = 'cookie.txt'
# # 声明一个mozillacookiejar对象实例来保存cookie 之后写入文
# cookie = cookielib.MozillaCookieJar(fileName)
# # 利用URilib库的httpcookieprocessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 创建一个请求，原理同urllib2的urlopen
# respones = opener.open("http://www.baidu.com")
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

# *******************获取cookie从文件**************
# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# req = urllib2.Request("http://www.baidu.com")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# respon = opener.open(req)
# print respon.read()

# # *******************利用cookie模拟网站登录*************
# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#     'stuid': '',
#     'pwd': ''
# })
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# result = opener.open(loginUrl, postdata)
# cookie.save(ignore_discard=True, ignore_expires=True)
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# result = opener.open(gradeUrl)
# print result.read()

# *************************正则表达式 *********************
# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo GGG')
result3 = re.match(pattern, 'helo aaaa')
result4 = re.match(pattern, 'hello afafa')
if result1:
    print result1.group()
else:
    print '1 匹配失败'

if result2:
    print result2.group()
else:
    print '2 匹配失败'
if result3:
    print result3.group()
else:
    print '3 匹配失败'
