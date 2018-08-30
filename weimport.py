# encoding: utf-8
import pymysql.cursors
from urllib import request
import ssl
from bs4 import BeautifulSoup as bs
import re
import math
ssl._create_default_https_context = ssl._create_unverified_context
#采集http://www.weimport.cn网站供需
#获取公司信息
def company_content_datas(url,types):
    lianxidata_content = bs(request.urlopen(url).read().decode("utf-8"), "html.parser")
    flo_d = lianxidata_content.find('div', {"class": "flo_d"})
    ul_data = flo_d.findAll("ul")
    info_all = []
    for ul_data_content in ul_data:
        company_name = ul_data_content.find("span", {"class": "mtext"})
        if (company_name):
            info_all.append(company_name.get_text())
        else:
            info = ul_data_content.findAll("li", {"class": "w_lx1"})
            for content_ul in info:
                info_all.append(content_ul.get_text())

    if re.search(r"^http:\/\/",info_all[7]):
        del info_all[7]

    if info_all[8].isdigit():
        all_data = info_all[:9]
    else:
        all_data = info_all[:8]
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='python',
                           charset='utf8')
    count = len(all_data)

    try:
        with conn.cursor() as cursor:
            sql = "insert into `weimport`(`company`,`name`,`tel`,`phone`,`fax`,`email`,`link`,`url`,`address`,`code`,`types`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            if count == 8:
                add = cursor.execute(sql, (
                    all_data[0], all_data[1], all_data[2], all_data[3], all_data[4], all_data[5], '', url,
                    all_data[7], '', str(types)))
                conn.commit()
                print(add)
                print(all_data)
            else:
                add = cursor.execute(sql, (
                all_data[0], all_data[1], all_data[2], all_data[3], all_data[4], all_data[5], all_data[6], url,
                all_data[7], all_data[8], str(types)))
                conn.commit()
                print(add)
                print(all_data)
    finally:
        conn.close()
    return 1

#获取列表数据
def company_list(url):
    cat_more_href_content = bs(request.urlopen(url).read().decode("utf-8"), "html.parser")
    types = cat_more_href_content.find("b").get_text()
    company = cat_more_href_content.find("div", {"id", "pics"})
    return company,types

resp = request.urlopen("http://www.weimport.cn/company/").read().decode("utf-8")
soup = bs(resp,"html.parser")
cat_more = soup.findAll("a",href=re.compile(r"http://www\.weimport\.cn/company/[0-9]{0,2}-1\.html"))
for cat_more_href in cat_more:
    company = company_list(cat_more_href['href'])
    company_list_href = cat_more_href['href']
    page_data = company[0].find("div",{"class":"inc-page-jump"})
    total = re.search("\d+$",re.search(r"总数: [\d]+", page_data.get_text()).group()).group()
    page_sum = math.ceil(int(total)/10)
    # print(a)
    # exit(1)
    # page_sum = len(page_data.findAll("a"))
    pattern = []
    # 第一页公司联系方式
    lianxi = company[0].findAll("a", href=re.compile(r"http://www.weimport.cn/show/[0-9]+/company\.html$"))
    for lianxidata in lianxi:
        company_content_datas(lianxidata["href"],company[1])

    if(page_sum>0):
        #整理剩余页
        for n in range(2,page_sum+2):
            pattern.append(re.sub(r'-[\d]+',str(-n), company_list_href))

        #循环剩余页
        for pattern_data in pattern:
            company = company_list(pattern_data)
            lianxi = company[0].findAll("a", href=re.compile(r"http://www.weimport.cn/show/[0-9]+/company\.html$"))
            for lianxidata in lianxi:
                company_content_datas(lianxidata["href"],company[1])
#            exit(3)
#    exit(2)
# exit(1)