# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import logging
import json
import re
import time

class StocksSpider(Spider):
    # 东方财富网股票
    name = 'stocks'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/']
    # search_url = ['http://32.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124011440659405328368_1575970432679&pn=1&pz=3880&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1575970432957']
    search_url = 'http://32.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124011440659405328368_1575970432679&pn={page}&pz=1&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1575970432957'


    def __init__(self):
        self.logging = logging.getLogger(__name__)

    def start_requests(self):
        url = self.search_url.format(page=1)
        yield Request(url=url,callback=self.parse)

    def parse(self, response):
        data = response.text
        data = re.findall('jQuery1124011440659405328368_1575970432679\((.*?)\)',data)
        for item in data:
            stocksSaveData = {}
            val = json.loads(item)
            stocksData = val['data']
            total = stocksData['total']
            diff = stocksData['diff']
            for diffItem in diff:
                stocksSaveData['stockNum'] = diffItem['f12']
                stocksSaveData['stockName'] = diffItem['f14']
                stocksSaveData['newPrice'] = diffItem['f2']
                stocksSaveData['zhangdiefu'] = diffItem['f3']
                stocksSaveData['zhangdiee'] = diffItem['f4']
                stocksSaveData['chengjiaoliang'] = diffItem['f5']
                stocksSaveData['chengjiaoe'] = diffItem['f6']
                stocksSaveData['zhengfu'] = diffItem['f7']
                stocksSaveData['zuogao'] = diffItem['f15']
                stocksSaveData['zuidi'] = diffItem['f16']
                stocksSaveData['jinkai'] = diffItem['f17']
                stocksSaveData['zuishou'] = diffItem['f18']
                stocksSaveData['liangbi'] = diffItem['f10']
                stocksSaveData['huangshoulv'] = diffItem['f8']
                stocksSaveData['shiyinglv'] = diffItem['f9']
                stocksSaveData['shijinglv'] = diffItem['f23']
                stocksSaveData['addData'] = json.dumps(diffItem)
                yield stocksSaveData

        for n in range(2,total + 1):
            time.sleep(2)
            url = self.search_url.format(page=n)
            yield Request(url=url, callback=self.parse_index)

    def parse_index(self, response):
        data = response.text
        data = re.findall('jQuery1124011440659405328368_1575970432679\((.*?)\)', data)
        for item in data:
            stocksSaveData = {}
            val = json.loads(item)
            stocksData = val['data']
            diff = stocksData['diff']
            for diffItem in diff:
                stocksSaveData['stockNum'] = diffItem['f12']
                stocksSaveData['stockName'] = diffItem['f14']
                stocksSaveData['newPrice'] = diffItem['f2']
                stocksSaveData['zhangdiefu'] = diffItem['f3']
                stocksSaveData['zhangdiee'] = diffItem['f4']
                stocksSaveData['chengjiaoliang'] = diffItem['f5']
                stocksSaveData['chengjiaoe'] = diffItem['f6']
                stocksSaveData['zhengfu'] = diffItem['f7']
                stocksSaveData['zuogao'] = diffItem['f15']
                stocksSaveData['zuidi'] = diffItem['f16']
                stocksSaveData['jinkai'] = diffItem['f17']
                stocksSaveData['zuishou'] = diffItem['f18']
                stocksSaveData['liangbi'] = diffItem['f10']
                stocksSaveData['huangshoulv'] = diffItem['f8']
                stocksSaveData['shiyinglv'] = diffItem['f9']
                stocksSaveData['shijinglv'] = diffItem['f23']
                stocksSaveData['addData'] = json.dumps(diffItem)
                yield stocksSaveData


