# -*- coding: utf-8 -*-
import scrapy
from quotetutorial.items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')

        '''
            如果标签里面只有一个内容
            1、quotes里面是个列表，获取第一个数据
            quotes[0]
            2、获取数据.css('.[classname]::text')
            3、获取数据内容.css('.text::text').extract()
        '''
        # print(quotes[0].css('.text::text').extract_first())quo

        '''
            如果标签里面有多个内容
            1、quotes里面是个列表，获取第一个数据
            quotes[0]
            2、获取数据.css('.[classname]::text')
            3、获取数据内容.css('.tags .tag::text').extract()
        '''
        # print(quotes[0].css('.tags .tag::text').extract())

        # 获取下一页地址
        next = response.css('.pager .next a::attr(href)').extract_first()
        # 构建完整的绝对URL
        url = response.urljoin(next)

        for quote in quotes:
            item = QuotetutorialItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        # 页面跳转，url指定跳转链接，callback,跳转后执行的方法
        yield scrapy.Request(url=url,callback=self.parse)