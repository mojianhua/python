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
	
	# scrapyd的使用
	1、安装scrapyd
		pip install scrapyd
		
		<!----scrapyd配置----!>
		# 网页和Json服务监听的IP地址，默认为127.0.0.1
		bind_address = 127.0.0.1
		# 监听的端口，默认为6800
		http_port   = 6800
		# 是否打开debug模式，默认为off
		debug       = off
		# 每个CPU可启用的Scrapy 进程数，默认为4
		max_proc_per_cpu = 4
		# 可启用的最多进程数，默认为0.如果未设置或者设为0，则使用的最多进程数=CPU数量*max_proc_per_cpu
		max_proc = 0
		# 项目eggs生成目录，默认为项目目录下eggs
		eggs_dir    = eggs
		# 项目日志生成目录，默认为项目目录下logs，如果不想要生成日志，可以直接设置成空
		logs_dir    = logs
		items_dir   =
		# 项目dbs生成目录，默认为项目目录下dbs
		dbs_dir     = dbs
		# 爬取的items存储的文件夹（版本0.15.以上），默认为空，不存储。
		items_dir =
		# 每个爬虫保持的完成任务数，默认为5.（版本0.15.以上，以前版本中为logs_to_keep）
		jobs_to_keep = 5
		# 保持的完成任务进程数。默认为100.（版本0.14.以上）
		finished_to_keep = 100
		# 轮训请求队列的时间间隔。默认为5s，可以为浮点数
		poll_interval = 5.0
		# 启动子进程的模块。可以使用自定义
		runner      = scrapyd.runner
		# 返回可用于twisted的application，可继承于Scrapyd添加和移除自己的组件和服务。 https://twistedmatrix.com/documents/current/core/howto/application.html查看更多
		application = scrapyd.app.application
		launcher    = scrapyd.launcher.Launcher
		# twisted的web资源，表示到scrapyd的接口。Scrapyd包含一个带有网站的界面，可以提供对应用程序的web资源的简单监视和访问。此设置必须提供twisted web资源的根类。
		webroot     = scrapyd.website.Root
	2、安装客户端
		pip install scrapyd_client
	3、添加爬虫
		scrapyd-deploy
	3.1、查看爬虫状态GET请求
		http://127.0.0.1:6800/daemonstatus.json
	3.2、获取上传爬虫目录
		curl http://127.0.0.1:6800/listprojects.json
	4、开始运行爬虫
	curl http://127.0.0.1:6800/schedule.json -d project=wangYiStocks -d spider=stocks
	
	project (string, required)，项目名称。
	spider (string, required)，爬虫名称，即 Spider下的name属性指定的。即scrapy crawl [爬虫名称]运行时的名称。
	setting (string, optional)，运行时的设置文件，默认为项目下settings.py。
	jobid (string, optional)，任务id，不指定则为默认生成的UUID。
	_version (string, optional)，运行的项目的版本。
	任何其他的参数都被传递给爬虫的属性，即scrapy crawl [爬虫名称] -a accounts=testAdmin后面-a所带的参数，在Spider中可通过self.testAdmin来获取值。
'''