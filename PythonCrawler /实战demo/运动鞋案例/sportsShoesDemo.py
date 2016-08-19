#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import urllib2
import re
import os

class SportsShoes:
    def __init__(self):
        self.siteURL = 'http://v.yupoo.com/photos/xuanfengyundong/albums/'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
    # 获取索引页面内容
    def getPage(self):
        url = self.siteURL
        # print url
        request = urllib2.Request(url,headers=self.headers)
        response = urllib2.urlopen(request)
        # print response.read().decode('utf-8')
        return response.read().decode('utf-8')
    # 获取鞋子标题和图片URL
    def getItemUrlAndTitle(self):
        page = self.getPage()
        pattern = re.compile('<h4><a class="Seta".*?href="(.*?)" title=.*?>(.*?)</a></h4>',re.S)
        items = re.findall(pattern,page)
        urlTitle = []
        for item in items:
            # print item[1],item[0]
            urlTitle.append([item[0],item[1]])
        return urlTitle
    #获取鞋子详情页面内容
    def getDetailPage(self,infoUrl):
        #大图页面URL
        url = infoUrl + "?style=story"
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')
    # 获取每个类型的所有图片
    def getAllImg(self,detailPage):
        pattern = re.compile('<img src="(.*?)" width=.*?/>')
        images = re.findall(pattern,detailPage)
        return images
    #保存图片
    def saveImgs(self,images,name):
        number = 1
        print u"发现",name,u"共有",len(images),u"张照片"
        for imageUrl in images:
            splitPath = imageUrl.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            filName = name + "/" + str(number) + '.' + fTail
            #保存单张图片
            self.saveImg(imageUrl,filName)
            number += 1
    #保存图片地址，文件名，保存单张图片
    def saveImg(self,imageUrl,fileName):
        request = urllib2.Request(imageUrl)
        u = urllib2.urlopen(request)
        data = u.read()
        f = open(fileName,'wb')
        f.write(data)
        print u"正悄悄保存鞋子图片",fileName
        f.close()
    #创建新目录
    def mkdir(self,path):
        path = path.strip()
        #判断路径是否存在
        isExists = os.path.exists(path)
        #p判断结果
        if not isExists:
            #如果不存在则创建目录
            print u"偷偷新建一个名字叫做",path,u"文件夹"
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建 并提示目录已存在
            print u"名为",path,"的文件夹已创建成功"
            return False
    #将所有鞋子的信息保存起来
    def savePageInfo(self):
        # 获取所有鞋子的detailURL 和 名字
        details = self.getItemUrlAndTitle()
        for item in details:
            print u"发现一类型鞋子，名字叫",item[1]
            print u"发现他的详细地址","http://v.yupoo.com" + item[0]
            print u"正在偷偷保存他的所有图片"
            # 鞋子的详细页面URL
            detailUrl = "http://v.yupoo.com" + item[0]
            # 得到鞋子详细地址的内容
            detailPage = self.getDetailPage(detailUrl)
            # 获取所有图片
            allImages = self.getAllImg(detailPage)
            # 创建目录
            self.mkdir(item[1])
            self.saveImgs(allImages,item[1])

sportShoes = SportsShoes()
sportShoes.savePageInfo()