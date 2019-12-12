'''
    1、新建项目
		scrapy startproject [项目名]
    2、创建模板
		scrapy genspider [模板名] [爬取的网站名]
	3、运行爬虫
		3.1：scrapy runspider [py文件]
		3.2：scrapy crawl [项目名]
	4、将爬虫结果以文件保存起来
		scrapy crawl quotes -o [文件名]
	5、目录结构
		setting ：存放基本配置
		pipeline ： 数据处理相关文件
		spider文件夹 : 存放爬虫文件
		items ：类似django的form，定义爬取的字段
		middleware ：中间层处理函数
		
	
	分布式scrapy-redis
	1、安装scrapy-redis
	pip install scrapy_redis
	2、详细使用看(wangYiStocks)项目
	
'''