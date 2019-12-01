# -*- coding: utf-8 -*-
import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']


    def make_requests_from_url(self, url):
        # download_timeout 超时设置
        return scrapy.Request(url=url,meta={'download_timeout': 0.00001},callback=self.parse)

    def parse(self, response):
        print(response.text)




