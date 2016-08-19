# -*- coding: utf-8 -*-

import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # print content
    pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2.*?' +
                         '<div.*?content">(.*?)</div>(.*?)' +
                         '<div.*?stats">.*?number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    # print '11111111111'
    for item in items:
        haveImg = re.search("img", item[2])
        if not haveImg:
            print item[0], item[1], item[3]
        # print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
# 正则表达式 解析
# 1）.*?
# 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到
# .*? 的搭配。

# 2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。

# 3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。

# 这样我们就获取了发布人，发布时间，发布内容，附加图片以及点赞数。
#
