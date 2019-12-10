# -*- coding: utf-8 -*-
import scrapy
import logging
import re

class Bangboer2Spider(scrapy.Spider):
    name = 'bangboer2'
    allowed_domains = ['www.bangboer.net']
    start_urls = ['http://www.bangboer.net/']
    search_url = 'https://www.bangboer.net/school/'
    urlList = ['l9c20','l24c20','l10c20']

    def __init__(self):
        self.logging = logging.getLogger(__name__)

    def start_requests(self):
        urlList = self.urlList
        for item in urlList:
            url = '{url}'.format(url=self.search_url)+ item
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
      page = response.css('.pages cite::text').re_first('(\d)页')
      schoolList = response.css('.catlist ul li .list_title a::attr(href)').extract()

      for url in schoolList:
          yield scrapy.Request(url=url, callback=self.info)

      for urlType in self.urlList:
          for pagsnum in range(2, int(page) + 1):
              url = '{url}{urlType}/{num}/'.format(url=self.search_url,num=pagsnum,urlType=urlType)
              yield scrapy.Request(url=url, callback=self.parse)

    def info(self,response):
        data = {}
        data['title'] = response.css('.title::text').extract_first()
        infoDatas = response.css('.basic ul li::text').extract()
        data['type'] = infoDatas[3]
        data['city'] = infoDatas[4]
        data['address'] = infoDatas[5]
        zhuanyeList = response.css('.tuijian .hot_major .list_title a::text').extract()
        addressList = response.css('.tuijian .hot_major .list_title p::text').re('地址：(.*)')
        if zhuanyeList:
            zhuanye = zhuanyeList[::2]
            xueli = zhuanyeList[1::2]
            zhuanyeData = {}

            num = 0
            for i in range(len(zhuanye)):
                zhuanyeData[num] = [zhuanye[num]]
                zhuanyeData[num].append(xueli[num])
                zhuanyeData[num].append(addressList[num])
                num += 1

            zhuanyeList = ''
            for item in zhuanyeData:
                zhuanyeList += '【' + ','.join(zhuanyeData[item]) + '】'

            data['zhuanyeList'] = zhuanyeList
        else:
            data['zhuanyeList'] = '无'
        yield data