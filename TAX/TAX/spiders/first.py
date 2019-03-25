import scrapy
import json


class QuerySpider(scrapy.Spider):
    name = "query"

    def start_requests(self):
        url1 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=5&rows=10&orgid=1320100&xzlb=1'
        url2 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=1&rows=10&orgid=1320102&xzlb=2'
        yield scrapy.Request(url=url1, callback=self.parse)

    def parse(self, response):
        # with open("/Users/vill/Desktop/test.html", "a+") as f:
        #     f.write(response.text)
        #     f.close()
        # pagelist = response.xpath("//ul[@id='pagelist_ul']")
        # lis = pagelist.xpath("//li")
        # for li in lis:
        #     print(li)
        # print(response.text)
        result = json.loads(response.text)
        currentPage = int(result["DATA"]["page"])
        totalPage = int(result["DATA"]["totalPage"])
        items = result["DATA"]["list"]
        # print(result)
        print(currentPage)
        print(totalPage)
        for item in items:
            nsrmc = item["xk_nsrmc"]
            nsrsbh = item["xk_xdr_swdj"]
            frmc = item["xk_fr"]
            tyshxym = item["xk_xdr_shxym"]
            print("%s: %s, %s, %s" % (frmc, nsrmc, nsrsbh, tyshxym))
        # 以下用来爬取本区域（例如南京市-鼓楼区）所有内容
        # if int(currentPage) <= int(totalPage):
        #     currentPage += 1
        #     url = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=%s&rows=10&orgid=1320100&xzlb=1' % currentPage
        #     yield scrapy.Request(url=url, callback=self.parse)


