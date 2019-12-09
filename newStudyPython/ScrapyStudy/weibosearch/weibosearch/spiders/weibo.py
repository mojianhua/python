# -*- coding: utf-8 -*-
from scrapy import Spider,FormRequest


class WeiboSpider(Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://weibo.cn/']
    search_url = 'https://weibo.cn/search/mblog'
    max_page = 100

    def start_requests(self):
        keyword = '0000001'
        # 组装url
        url = '{url}?keyword={keyword}'.format(url=self.search_url,keyword=keyword)

        # 组装表格提交数据
        for page in range (self.max_page + 1):
            data ={
                'hideSearchFrame':'',
                'keyword': keyword,
                'page':str(page)
            }

            # 表格提交，url：需要提交的链接，callback：处理数据的方法，formdata:需要提交的数据
            yield FormRequest(url=url,callback=self.parse_index,formdata=data)

    def parse_index(self, response):
        print(response.text)
