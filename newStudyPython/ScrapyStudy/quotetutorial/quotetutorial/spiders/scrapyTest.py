# -*- coding: utf-8 -*-
import scrapy


class ScrapytestSpider(scrapy.Spider):
    # 项目名称
    name = 'scrapyTest'
    # 域名
    allowed_domains = ['doc.scrapy.org']
    # 初始化url
    start_urls = ['http://doc.scrapy.org/en/latest/_static/selectors-sample1.html']

    def parse(self, response):
        # 获取a标签里面的内容
        text = response.css('a::text').extract()
        # 获取a标签里面href属性
        hrefs = response.css('a::attr(href)').extract()
        # 获取a标签里面href属性包含image的属性
        hrefs = response.css('a[href*=image]::attr(href)').extract()
        # 获取a标签里面href属性包含imageabc的属性,页码不存在的所有报空
        hrefs = response.css('a[href*=imageabc]::attr(href)').extract()
        # 获取a标签里面img的src属性
        srcs = response.css('a[href*=image] img::attr(src)').extract()
        # 正则使用，获取a标签里面Name后的内容
        re1 = response.css('a::text').re('Name\:(.*)')
        # 正则使用2，获取a标签里面img标签src里面的图片，不带缩略图标志
        re1 = response.css('a img::attr(src)').re('(.*)_thumb')
        # 正则使用3，获取a标签里面img第一个src里面的图片，不带缩略图标志
        re1 = response.css('a img::attr(src)').re_first('(.*)_thumb')
        print(re1)