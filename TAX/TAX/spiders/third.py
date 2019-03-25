import scrapy
import json


class QuerySpider(scrapy.Spider):
    name = "query2"

    def start_requests(self):
        # url1 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=5&rows=10&orgid=1320100&xzlb=1'
        url2 = 'https://www.qichacha.com/search?key=91320191MA1X2RWT4D'
        yield scrapy.Request(url=url2, callback=self.parse)

    def parse(self, response):
        a = response.xpath("//*[@id='search-result']")
        gsname = a.xpath("//a[@class='ma_h1']/text()")[0].extract()
        frname = a.xpath('//tr/td/p[@class="m-t-xs"]/a[@class="text-primary"]/text()')[0].extract()
        ziben = a.xpath('//tr/td/p[@class="m-t-xs"]')
        zczb = ziben[0].xpath('//tr/td/p[@class="m-t-xs"]/span').xpath("string(.)").extract()[0]
        clsj = ziben[0].xpath('//tr/td/p[@class="m-t-xs"]/span').xpath("string(.)").extract()[1]
        dh = ziben[0].xpath('//tr/td/p[@class="m-t-xs"]/span').xpath("string(.)").extract()[2]
        dz = ziben[0].xpath('///tr/td/p[@class="m-t-xs"]').xpath('string(.)').extract()[2].replace(" ", "").replace("\n", "")
        print("%s : %s: %s, %s, %s, %s" % (gsname, frname, zczb, clsj, dh, dz))

        # for i in ziben:
        #     fr = a.xpath('//a/text()')[0].extract()
        #     print(fr)
            # print(i.xpath("string(.)").extract())

        #print(ziben)
        # with open("/Users/vill/Desktop/test.html", "a+") as f:
        #     f.write(response.text)
        #     f.close()



