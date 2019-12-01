# -*- coding: utf-8 -*-
import scrapy


class F2cSpider(scrapy.Spider):
    name = 'f2c'
    allowed_domains = ['port.food2china.com']
    start_urls = ['http://port.food2china.com/']

    # 命令行里传参接收参数,调用方式：scrapy crawl f2c -a one=11111
    # 多个参数用多个a连接起来如：scrapy crawl f2c -a one=11111 -a two=2222
    def __init__(self,one=None,*args,**kwargs):
        super(F2cSpider,self).__init__(*args,**kwargs)
        self.one = one

    '''
        这个方法接收一个链接，返回一个Request对象。
    '''
    def make_requests_from_url(self, url):
        return scrapy.Request(url=url,callback=self.parse_index)

    def parse(self, response):
        self.logger.info(self.one)

    def parse_index(self,response):
        # log类，打印信息
        self.logger.info(self.one)
