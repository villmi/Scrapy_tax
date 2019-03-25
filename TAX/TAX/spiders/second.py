import scrapy
import json


class QuerySpider(scrapy.Spider):
    name = "query1"

    def start_requests(self):
        # url1 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=5&rows=10&orgid=1320100&xzlb=1'
        url2 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=1&rows=10&orgid=1320102&xzlb=2'
        yield scrapy.Request(url=url2, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        currentPage = int(result["DATA"]["page"])
        totalPage = int(result["DATA"]["totalPage"])
        items = result["DATA"]["list"]
        # print(result)
        print(currentPage)
        print(totalPage)
        for item in items:
            ajmc = item["cf_ajmc"]
            cfsy= item["cf_sy"]
            cfyj = item["cf_yj"]
            cfjg = item["cf_jg"]
            djrq = item["cf_sxq"]
            cfxzjg = item["cf_xzjg"]
            print("%s: %s, %s, %s, %s, %s" % (ajmc, cfsy, cfyj, cfjg, djrq, cfxzjg))
        # 以下用来爬取本区域（例如南京市-鼓楼区）所有内容
        # if int(currentPage) <= int(totalPage):
        #     currentPage += 1
        #     url = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=%s&rows=10&orgid=1320100&xzlb=1' % currentPage
        #     yield scrapy.Request(url=url, callback=self.parse)


