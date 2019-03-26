import scrapy
import json

city_code = [13201, 13202, 13203, 13204, 13205, 13206, 13207, 13208, 13209, 13210, 13211, 13212, 13213, 13214, 13215,
             13216, 13217]
# city_code = [13201]

dic_js = '{"13209":[{"sjxzqh_dm":"13209","xzqh_dm":"1320900","xzqh_mc":"市本级"},{"sjxzqh_dm":"13209","xzqh_dm":"1320903","xzqh_mc":"盐都区"},{"sjxzqh_dm":"13209","xzqh_dm":"1320921","xzqh_mc":"响水县"},{"sjxzqh_dm":"13209","xzqh_dm":"1320922","xzqh_mc":"滨海县"},{"sjxzqh_dm":"13209","xzqh_dm":"1320923","xzqh_mc":"阜宁县"},{"sjxzqh_dm":"13209","xzqh_dm":"1320924","xzqh_mc":"射阳县"},{"sjxzqh_dm":"13209","xzqh_dm":"1320925","xzqh_mc":"建湖县"},{"sjxzqh_dm":"13209","xzqh_dm":"1320981","xzqh_mc":"东台市"},{"sjxzqh_dm":"13209","xzqh_dm":"1320982","xzqh_mc":"大丰区"}],"13208":[{"sjxzqh_dm":"13208","xzqh_dm":"1320800","xzqh_mc":"市本级"},{"sjxzqh_dm":"13208","xzqh_dm":"1320803","xzqh_mc":"淮安区"},{"sjxzqh_dm":"13208","xzqh_dm":"1320804","xzqh_mc":"淮阴区"},{"sjxzqh_dm":"13208","xzqh_dm":"1320826","xzqh_mc":"涟水县"},{"sjxzqh_dm":"13208","xzqh_dm":"1320829","xzqh_mc":"洪泽区"},{"sjxzqh_dm":"13208","xzqh_dm":"1320830","xzqh_mc":"盱眙县"},{"sjxzqh_dm":"13208","xzqh_dm":"1320831","xzqh_mc":"金湖县"}],"13207":[{"sjxzqh_dm":"13207","xzqh_dm":"1320700","xzqh_mc":"市本级"},{"sjxzqh_dm":"13207","xzqh_dm":"1320721","xzqh_mc":"赣榆区"},{"sjxzqh_dm":"13207","xzqh_dm":"1320722","xzqh_mc":"东海县"},{"sjxzqh_dm":"13207","xzqh_dm":"1320723","xzqh_mc":"灌云县"},{"sjxzqh_dm":"13207","xzqh_dm":"1320724","xzqh_mc":"灌南县"}],"13216":[{"sjxzqh_dm":"13216","xzqh_dm":"1321600","xzqh_mc":"张家港保税区"}],"13206":[{"sjxzqh_dm":"13206","xzqh_dm":"1320600","xzqh_mc":"市本级"},{"sjxzqh_dm":"13206","xzqh_dm":"1320621","xzqh_mc":"海安市"},{"sjxzqh_dm":"13206","xzqh_dm":"1320623","xzqh_mc":"如东县"},{"sjxzqh_dm":"13206","xzqh_dm":"1320681","xzqh_mc":"启东市"},{"sjxzqh_dm":"13206","xzqh_dm":"1320682","xzqh_mc":"如皋市"},{"sjxzqh_dm":"13206","xzqh_dm":"1320684","xzqh_mc":"海门市"}],"13205":[{"sjxzqh_dm":"13205","xzqh_dm":"1320500","xzqh_mc":"市本级"},{"sjxzqh_dm":"13205","xzqh_dm":"1320506","xzqh_mc":"吴中区"},{"sjxzqh_dm":"13205","xzqh_dm":"1320507","xzqh_mc":"相城区"},{"sjxzqh_dm":"13205","xzqh_dm":"1320508","xzqh_mc":"姑苏区"},{"sjxzqh_dm":"13205","xzqh_dm":"1320581","xzqh_mc":"常熟市"},{"sjxzqh_dm":"13205","xzqh_dm":"1320582","xzqh_mc":"张家港市"},{"sjxzqh_dm":"13205","xzqh_dm":"1320583","xzqh_mc":"昆山市"},{"sjxzqh_dm":"13205","xzqh_dm":"1320584","xzqh_mc":"吴江区"},{"sjxzqh_dm":"13205","xzqh_dm":"1320585","xzqh_mc":"太仓市"}],"13204":[{"sjxzqh_dm":"13204","xzqh_dm":"1320400","xzqh_mc":"市本级"},{"sjxzqh_dm":"13204","xzqh_dm":"1320412","xzqh_mc":"武进区"},{"sjxzqh_dm":"13204","xzqh_dm":"1320481","xzqh_mc":"溧阳市"},{"sjxzqh_dm":"13204","xzqh_dm":"1320482","xzqh_mc":"金坛区"}],"13217":[{"sjxzqh_dm":"13217","xzqh_dm":"1321700","xzqh_mc":"苏州工业园区"}],"13212":[{"sjxzqh_dm":"13212","xzqh_dm":"1321200","xzqh_mc":"市本级"},{"sjxzqh_dm":"13212","xzqh_dm":"1321281","xzqh_mc":"兴化市"},{"sjxzqh_dm":"13212","xzqh_dm":"1321282","xzqh_mc":"靖江市"},{"sjxzqh_dm":"13212","xzqh_dm":"1321283","xzqh_mc":"泰兴市"},{"sjxzqh_dm":"13212","xzqh_dm":"1321284","xzqh_mc":"姜堰区"}],"13203":[{"sjxzqh_dm":"13203","xzqh_dm":"1320300","xzqh_mc":"市本级"},{"sjxzqh_dm":"13203","xzqh_dm":"1320305","xzqh_mc":"贾汪区"},{"sjxzqh_dm":"13203","xzqh_dm":"1320321","xzqh_mc":"丰县"},{"sjxzqh_dm":"13203","xzqh_dm":"1320322","xzqh_mc":"沛县"},{"sjxzqh_dm":"13203","xzqh_dm":"1320323","xzqh_mc":"铜山区"},{"sjxzqh_dm":"13203","xzqh_dm":"1320324","xzqh_mc":"睢宁县"},{"sjxzqh_dm":"13203","xzqh_dm":"1320381","xzqh_mc":"新沂市"},{"sjxzqh_dm":"13203","xzqh_dm":"1320382","xzqh_mc":"邳州市"}],"13211":[{"sjxzqh_dm":"13211","xzqh_dm":"1321100","xzqh_mc":"市本级"},{"sjxzqh_dm":"13211","xzqh_dm":"1321112","xzqh_mc":"丹徒区"},{"sjxzqh_dm":"13211","xzqh_dm":"1321181","xzqh_mc":"丹阳市"},{"sjxzqh_dm":"13211","xzqh_dm":"1321182","xzqh_mc":"扬中市"},{"sjxzqh_dm":"13211","xzqh_dm":"1321183","xzqh_mc":"句容市"}],"13202":[{"sjxzqh_dm":"13202","xzqh_dm":"1320200","xzqh_mc":"市本级"},{"sjxzqh_dm":"13202","xzqh_dm":"1320205","xzqh_mc":"锡山区"},{"sjxzqh_dm":"13202","xzqh_dm":"1320206","xzqh_mc":"惠山区"},{"sjxzqh_dm":"13202","xzqh_dm":"1320211","xzqh_mc":"滨湖区"},{"sjxzqh_dm":"13202","xzqh_dm":"1320281","xzqh_mc":"江阴市"},{"sjxzqh_dm":"13202","xzqh_dm":"1320282","xzqh_mc":"宜兴市"},{"sjxzqh_dm":"13202","xzqh_dm":"1320298","xzqh_mc":"高新区"}],"13201":[{"sjxzqh_dm":"13201","xzqh_dm":"1320100","xzqh_mc":"市本级"},{"sjxzqh_dm":"13201","xzqh_dm":"1320102","xzqh_mc":"玄武区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320104","xzqh_mc":"秦淮区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320105","xzqh_mc":"建邺区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320106","xzqh_mc":"鼓楼区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320111","xzqh_mc":"浦口区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320112","xzqh_mc":"江北新区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320113","xzqh_mc":"栖霞区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320114","xzqh_mc":"雨花台区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320115","xzqh_mc":"江宁区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320116","xzqh_mc":"六合区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320124","xzqh_mc":"溧水区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320125","xzqh_mc":"高淳区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320137","xzqh_mc":"经开区"},{"sjxzqh_dm":"13201","xzqh_dm":"1320139","xzqh_mc":"江宁经开"}],"13213":[{"sjxzqh_dm":"13213","xzqh_dm":"1321300","xzqh_mc":"市本级"},{"sjxzqh_dm":"13213","xzqh_dm":"1321311","xzqh_mc":"宿豫区"},{"sjxzqh_dm":"13213","xzqh_dm":"1321322","xzqh_mc":"沭阳县"},{"sjxzqh_dm":"13213","xzqh_dm":"1321323","xzqh_mc":"泗阳县"},{"sjxzqh_dm":"13213","xzqh_dm":"1321324","xzqh_mc":"泗洪县"}],"13210":[{"sjxzqh_dm":"13210","xzqh_dm":"1321000","xzqh_mc":"市本级"},{"sjxzqh_dm":"13210","xzqh_dm":"1321003","xzqh_mc":"邗江区"},{"sjxzqh_dm":"13210","xzqh_dm":"1321023","xzqh_mc":"宝应县"},{"sjxzqh_dm":"13210","xzqh_dm":"1321081","xzqh_mc":"仪征市"},{"sjxzqh_dm":"13210","xzqh_dm":"1321084","xzqh_mc":"高邮市"},{"sjxzqh_dm":"13210","xzqh_dm":"1321088","xzqh_mc":"江都区"},{"sjxzqh_dm":"13210","xzqh_dm":"1321092","xzqh_mc":"广陵区"}]}'


class QuerySpider(scrapy.Spider):
    name = "query"

    def start_requests(self):
        city_code.sort(reverse=True)
        city = city_code[0]
        print(len(city_code))
        js = json.loads(dic_js)
        location = js["%s" % city]
        code = location[0]["xzqh_dm"]
        url1 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=1&rows=10&orgid=%s&xzlb=1' % code
        url2 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=1&rows=10&orgid=1320102&xzlb=2'
        yield scrapy.Request(url=url1, callback=self.parse, meta={'count': 0,
                                                                  'city': city,
                                                                  'city_index': 0,
                                                                  'code': code})
        'count 表示地级市的区计数' \
        'city 表示地级市编码' \
        'city_index 表示地级市计数'

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
        code = response.meta["code"]
        # print(result)
        print(currentPage)
        print(totalPage)
        f = open('/Users/vill/Desktop/TAX/%s.data' % code, 'a+')
        for item in items:
            nsrmc = item["xk_nsrmc"]
            nsrsbh = item["xk_xdr_swdj"]
            frmc = item["xk_fr"]
            tyshxym = item["xk_xdr_shxym"]
            f.write("%s,%s,%s,%s\n" % (frmc, nsrmc, nsrsbh, tyshxym))
            print("%s: %s, %s, %s" % (frmc, nsrmc, nsrsbh, tyshxym))
        print(len(city_code))
        # 以下用来爬取本区域（例如南京市-鼓楼区）所有内容
        count = response.meta["count"]
        city = response.meta["city"]
        city_index = response.meta["city_index"]
        js = json.loads(dic_js)
        location = js["%s" % city]
        code = location[int(count)]["xzqh_dm"]
        print(count)
        js = json.loads(dic_js)
        if int(currentPage) <= int(totalPage):
            if int(currentPage) < int(totalPage):
                currentPage += 1
                url = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=%s&rows=10&orgid=%s&xzlb=1' % (currentPage, code)
                yield scrapy.Request(url=url, callback=self.parse, meta={'count': count,
                                                                         'city': city,
                                                                         'city_index': int(city_index),
                                                                         'code': code})
            if int(currentPage) == int(totalPage):
                count = int(count) + 1
                location = js["%s" % city]
                if count < len(location) and count < len(location):
                    code = location[count]["xzqh_dm"]
                    url1 = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=1&rows=10&orgid=%s&xzlb=1' % code
                    yield scrapy.Request(url=url1, callback=self.parse, meta={'count': count,
                                                                              'city': city,
                                                                              'city_index': int(city_index),
                                                                              'code': code})
                else:
                    city_index += int(city_index) + 1
                    city = city_code[city_index]
                    js = json.loads(dic_js)
                    location = js["%s" % city]
                    count = 0
                    code = location[int(count)]["xzqh_dm"]
                    url = 'https://etax.jsgs.gov.cn/portal/queryapi/queryPageList.do?page=1&rows=10&orgid=%s&xzlb=1' % code
                    yield scrapy.Request(url=url, callback=self.parse, meta={'count': count,
                                                                             'city': city,
                                                                             'city_index': int(city_index),
                                                                             'code': code})




