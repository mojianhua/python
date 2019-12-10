# -*- coding: utf-8 -*-
from scrapy import Spider,FormRequest


class StocksSpider(Spider):
    name = 'stocks'
    allowed_domains = ['quote.eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/']
    search_url = ['http://32.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124011440659405328368_1575970432679&pn=1&pz=3880&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1575970432957']

    def start_requests(self):
        for item in self.search_url:
            data = {
                'cb': 'jQuery1124011440659405328368_1575970432679',
                'pn': str(1),
                'pz': str(3880),
                'po': str(1),
                'np': str(1),
                'ut': ' bd1d9ddb04089700cf9c27f6f7426281',
                'fltt': str(2),
                'invt': str(2),
                'fid': 'f3',
                'fs': 'm:0 t:6,m:0 t:13,m:0 t:80,m:1 t:2,m:1 t:23',
                'fields':'f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f12, f13, f14, f15, f16, f17, f18, f20, f21, f23, f24, f25, f22, f11, f62, f128, f136, f115, f152',
                '_':'1575970432957'
            }
            yield FormRequest(url=item,callback=self.parse,formdata=data)

    def parse(self, response):
        print(response.text)
