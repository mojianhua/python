# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    '''
        该方法必须返回一个可迭代对象（iterable）。该对象包含了spider用于抓取的第一个Request。
        当spider起订抓取并且未指定url时，该方法被调用。当指定了url时，make_requests_from_url()将被调用来创建request对象。该方法仅仅会被scrapy调用一次，因此您可以将其实现为生成器。
    '''
    def start_requests(self):
        yield scrapy.Request(url='http://httpbin.org/post',method='POST',callback=self.parse_post)

    def parse(self, response):
        pass

    def parse_post(self,resopnse):
        print('Hello',resopnse.status)