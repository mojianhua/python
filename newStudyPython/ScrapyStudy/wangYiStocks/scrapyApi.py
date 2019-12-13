from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI('http://127.0.0.1:6800')
# 获取上传爬虫目录
list_projects = scrapyd.list_projects()
print(list_projects)
list_spiders = scrapyd.list_spiders('wangYiStocks')
# 查看爬虫任务
print(list_spiders)
# 查看项目任务id
list_jobs = scrapyd.list_jobs('wangYiStocks')
print(list_jobs)
cancel = scrapyd.cancel('wangYiStocks','7c8be8661d4c11ea95d06c4b903122b5')
print(cancel)