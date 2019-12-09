# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BangboerPipeline(object):
    def __init__(self, host, port, user, password, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

        # 从setting里面获取变量

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('DB_HOST'),
            port=crawler.settings.get('DB_PORT'),
            user=crawler.settings.get('DB_USER'),
            password=crawler.settings.get('DB_PASSWORD'),
            database=crawler.settings.get('DB_DATABASE'),
            charset=crawler.settings.get('DB_CHARSET'),
        )

    # 开启爬虫时执行，只执行一次
    def open_spider(self, spider):
        connect = {
            'host': self.host,
            'port': self.port,
            'user': self.user,
            'password': self.password,
            'database': self.database,
            'charset': self.charset
        }
        self.conn = pymysql.connect(**connect)
        self.cursor = self.conn.cursor()

    # 处理提取的数据(保存数据)
    def process_item(self, item, spider):
        print('----------------------------------------------------------------------------------------------------')
        self.cursor.execute("insert into school (title, `type`, city, address,zhuanyeList) values (%s, %s, %s,%s,%s)",(item["title"], item["type"], item["city"], item["address"],item["zhuanyeList"]))
        self.conn.commit()
        print('----------------------------------------------------------------------------------------------------')
        return item

    # 爬虫最后执行
    def close_spider(self, spider):
        self.conn.close()
