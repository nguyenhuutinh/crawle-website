from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
from scrapy.http import Request
import lxml.html.clean as clean

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ['ruoutaychinhhang.com']
    start_urls = [
        'https://ruoutaychinhhang.com/san-pham',
        'https://ruoutaychinhhang.com/san-pham?page=2',
        'https://ruoutaychinhhang.com/san-pham?page=3',
        'https://ruoutaychinhhang.com/san-pham?page=4',
        'https://ruoutaychinhhang.com/san-pham?page=5',
        'https://ruoutaychinhhang.com/san-pham?page=6',
        'https://ruoutaychinhhang.com/san-pham?page=7',
        'https://ruoutaychinhhang.com/san-pham?page=8',
        'https://ruoutaychinhhang.com/san-pham?page=9',
        'https://ruoutaychinhhang.com/san-pham?page=10',
        'https://ruoutaychinhhang.com/san-pham?page=11',
        'https://ruoutaychinhhang.com/san-pham?page=12',
        'https://ruoutaychinhhang.com/san-pham?page=13',
        'https://ruoutaychinhhang.com/san-pham?page=14',
        'https://ruoutaychinhhang.com/san-pham?page=15',
        'https://ruoutaychinhhang.com/san-pham?page=16',
        'https://ruoutaychinhhang.com/san-pham?page=17',
        'https://ruoutaychinhhang.com/san-pham?page=18',
        'https://ruoutaychinhhang.com/san-pham?page=19',
        'https://ruoutaychinhhang.com/san-pham?page=20',
        'https://ruoutaychinhhang.com/san-pham?page=21',
        'https://ruoutaychinhhang.com/san-pham?page=22',
        'https://ruoutaychinhhang.com/san-pham?page=23',
        'https://ruoutaychinhhang.com/san-pham?page=24',
        'https://ruoutaychinhhang.com/san-pham?page=25',
        'https://ruoutaychinhhang.com/san-pham?page=26',
        'https://ruoutaychinhhang.com/san-pham?page=27',
        'https://ruoutaychinhhang.com/san-pham?page=28',
        'https://ruoutaychinhhang.com/san-pham?page=29',
        'https://ruoutaychinhhang.com/san-pham?page=30',
        'https://ruoutaychinhhang.com/san-pham?page=31',
        'https://ruoutaychinhhang.com/san-pham?page=32',
        'https://ruoutaychinhhang.com/san-pham?page=33',
        'https://ruoutaychinhhang.com/san-pham?page=34',
        'https://ruoutaychinhhang.com/san-pham?page=35',
        'https://ruoutaychinhhang.com/san-pham?page=36',
        'https://ruoutaychinhhang.com/san-pham?page=37',
        'https://ruoutaychinhhang.com/san-pham?page=38',
        'https://ruoutaychinhhang.com/san-pham?page=39',
        'https://ruoutaychinhhang.com/san-pham?page=40',
        'https://ruoutaychinhhang.com/san-pham?page=41',
    ]
    count = 1

    custom_settings = {

    'LOG_LEVEL': 'INFO',
 
    }
    
    def parse(self, response):
        # print("hello1")
        for result in response.xpath('//*[contains(@class,"product-item")]'):
            # print("hello2")
            # for page in range(1, 18):
            
            ref = result.xpath('.//div[contains(@class,"product-attribute")]/a/@href').get().replace("./","")
            url = f"https://ruoutaychinhhang.com/{ref}" 
        #     print(url)
            yield Request(url, self.parse_next_page)

        return  




    def parse_next_page(self, response):
        item = CrawlerItem()
        item["ID"] = self.count
        item["ptype"] = "simple"
        item["productcode"] = ""
        item['title'] = response.xpath('//form[@id="buy-form"]/div[@class="detail"]/h1/text()').extract_first()
        item["public"] = 1
        item["featured"] = 0
        item["displayInCat"] = "visible"
        item["shortDes"] = ""
       
        safe_attrs = set(['src', 'alt', 'href', 'title'])

        # converter = html2text.HTML2Text()
        des = response.xpath(
                '//div[@class="content-detail"]').extract_first().replace("href=\"https://ruoutaychinhhang.com","href=\"http://ruounhapchinhhang.com").replace("Rượu Tây Chính Hãng", "Rượu Nhập Chính Hãng").replace(" 182 - 184 Hải Thượng Lãn Ông, P.10, Q.5, TP.HCM"," 33 ĐIỆN BIÊN PHỦ P. PHƯỚC HƯNG, TP BÀ RỊA, TỈNH BÀ RỊA – VŨNG TÀU").replace(" 0931 97 39 97", " 093.123.72.72").replace("ruouhamyxuan@gmail.com","ruounhapchinhhang.vn@gmail.com").replace("https://www.facebook.com/ruoungoainhapDL/","https://www.facebook.com/ruounhapchinhhang.vn/")
        cleaner = clean.Cleaner(safe_attrs=safe_attrs)
        cleaned_html = cleaner.clean_html(des)
        # print(cleaned_html)
        item["longDes"] = cleaned_html
        item["promoStartDate"] = ""
        item["promoEndDate"] = ""
        item["taxStatus"] = ""
        item["tax"] = response.xpath(
                '//span[@class="pb-stt"]/text()').extract_first().strip()
        item["instock"] = "1" if response.xpath(
                '//span[@class="pb-stt"]/text()').extract_first().strip() == "Còn hàng" else "0"
                                
        item["houseware"] = ""
        item["limited"] = ""
        item["bookavailable"] = ""
        item["privatesale"] = ""
        item["weight"] = ""
        item["longwidth"] = ""
        item["thinwidth"] = ""
        item["height"] = ""
        item["commentable"] = ""
        item["paymentnote"] = ""
        item["saleprice"] = ""
        item["price"] = response.xpath('//p[@class="price"]/@price').extract_first()
        info = response.xpath(
                '//form[@id="buy-form"]/div[@class="detail"]/div[@class="tag"]/ul/li/text()').getall()
        infoChild = response.xpath(
                '//form[@id="buy-form"]/div[@class="detail"]/div[@class="tag"]/ul/li/a/text()').getall()
        
        for i in info:
         if(i.startswith("\n")):
                info.remove(i)

        # print(infoChild)
        # print("--------------")
        # print("--------------")
        # print(info)
        # print("--||||||||||------------")
        if len(info) > 0 and info[0].startswith("Thương hiệu"):
                thuonghieu = infoChild[0]
        elif len(info) > 1 and info[1].startswith("Thương hiệu"): 
                thuonghieu = infoChild[1]
        elif len(info) > 2 and info[2].startswith("Thương hiệu"): 
                thuonghieu = infoChild[2]
        elif len(info) > 3 and info[3].startswith("Thương hiệu"): 
                thuonghieu = infoChild[3]
        elif len(info) > 4 and info[4].startswith("Thương hiệu"): 
                thuonghieu = infoChild[4]
        elif len(info) > 5 and  info[5].startswith("Thương hiệu"): 
                thuonghieu = infoChild[5]
        else:     thuonghieu = ""

        # print("thuonghieu")
        # print(thuonghieu)

        if len(info) > 0 and info[0].startswith("Dung Tích"):
                dungtich = infoChild[0]
        elif len(info) > 1 and info[1].startswith("Dung Tích"): 
                dungtich = infoChild[1]
        elif len(info) > 2 and info[2].startswith("Dung Tích"): 
                dungtich = infoChild[2]
        elif len(info) > 3 and info[3].startswith("Dung Tích"): 
                dungtich = infoChild[3]
        elif len(info) > 4 and info[4].startswith("Dung Tích"): 
                dungtich = infoChild[4]
        elif len(info) > 5 and  info[5].startswith("Dung Tích"): 
                dungtich = infoChild[5]
        else:     dungtich = ""
        # print("dungtich")
        # print(dungtich)

        if len(info) > 0 and info[0].startswith("Nồng Độ"):
                nongdo = infoChild[0]
        elif len(info) > 1 and info[1].startswith("Nồng Độ"): 
                nongdo = infoChild[1]
        elif len(info) > 2 and info[2].startswith("Nồng Độ"): 
                nongdo = infoChild[2]
        elif len(info) > 3 and info[3].startswith("Nồng Độ"): 
                nongdo = infoChild[3]
        elif len(info) > 4 and info[4].startswith("Nồng Độ"): 
                nongdo = infoChild[4]
        elif len(info) > 5 and  info[5].startswith("Nồng Độ"): 
                nongdo = infoChild[5]
        else:     nongdo = ""

        # print("nongdo")
        # print(nongdo)


        if len(info) > 0 and info[0].startswith("Tuổi Rượu"):
                tuouruou = infoChild[0]
        elif len(info) > 1 and info[1].startswith("Tuổi Rượu"): 
                tuouruou = infoChild[1]
        elif len(info) > 2 and info[2].startswith("Tuổi Rượu"): 
                tuouruou = infoChild[2]
        elif len(info) > 3 and info[3].startswith("Tuổi Rượu"): 
                tuouruou = infoChild[3]
        elif len(info) > 4 and info[4].startswith("Tuổi Rượu"): 
                tuouruou = infoChild[4]
        elif len(info) > 5 and  info[5].startswith("Tuổi Rượu"): 
                tuouruou = infoChild[5]
        else:     tuouruou = ""

        # print("tuouruou")
        # print(tuouruou)

        if len(info) > 0 and info[0].startswith("Xuất xứ"):
                xuatxu = infoChild[0]
        elif len(info) > 1 and info[1].startswith("Xuất xứ"): 
                xuatxu = infoChild[1]
        elif len(info) > 2 and info[2].startswith("Xuất xứ"): 
                xuatxu = infoChild[2]
        elif len(info) > 3 and info[3].startswith("Xuất xứ"): 
                xuatxu = infoChild[3]
        elif len(info) > 4 and info[4].startswith("Xuất xứ"): 
                xuatxu = infoChild[4]
        elif len(info) > 5 and  info[5].startswith("Xuất xứ"): 
                xuatxu = infoChild[5]
        else:     xuatxu = ""
        
        # print("xuatxu")
        # print(xuatxu)


        if len(info) > 0 and info[0].startswith("Phân Loại"):
                phanloai = infoChild[0]
        elif len(info) > 1 and info[1].startswith("Phân Loại"): 
                phanloai = infoChild[1]
        elif len(info) > 2 and info[2].startswith("Phân Loại"): 
                phanloai = infoChild[2]
        elif len(info) > 3 and info[3].startswith("Phân Loại"): 
                phanloai = infoChild[3]
        elif len(info) > 4 and info[4].startswith("Phân Loại"): 
                phanloai = infoChild[4]
        elif len(info) > 5 and  info[5].startswith("Phân Loại"): 
                phanloai = infoChild[5]
        else:     phanloai = ""

        # print("phanloai")
        # print(phanloai)

        item["category"] = response.xpath(
                '//div[@class="container"]/ul/li/a/span/text()').getall()[1].strip()
        tags = response.xpath('//div[@class="image-detail"]/div/a/i[@class="fas fa-asterisk"]/../text()').getall()
        
        # print(','.join(tags).replace("\n","").replace("  ","").strip() if len(tags) > 0 else "" )
        item["tags"] =  ','.join(tags).replace("\n","").replace("  ","").strip() if len(tags) > 0 else "" 
        item["shippingclass"] = ""
        
        item['image'] =  response.xpath(
                '//div[@class="image-detail"]/img/@src').extract_first()
        item["downloadavailable"] = ""
        item["downloadenddate"] = ""
        item["org"] = ""
        item["group"] = ""
        item["upsell"] = ""
        item["bancheo"] = ""
        item["urlngoai"] = ""
        item["content"] = ""
        item["location"] = ""
        # print ("special prd", response.url ) if len(info) < 4 else ""
        item["field1name"] = "Dung Tích"
        item["field1value"] = dungtich
        item["field1display"] = "1"
        item["field1global"] = "1"
        item["field2name"] = "Nồng Độ"
        item["field2value"] = nongdo
        item["field2display"] = "1"
        item["field2global"] = "1"
        item["field3name"] = "Tuổi Rượu"
        item["field3value"] = tuouruou
        item["field3display"] = "1"
        item["field3global"] = "1"
        item["field4name"] = "Thương Hiệu"
        item["field4value"] = thuonghieu
        item["field4display"] = "1"
        item["field4global"] = "1"
        item["field5name"] = "Xuất xứ"
        item["field5value"] = xuatxu
        item["field5display"] = "1"
        item["field5global"] = "1"
        item["field6name"] = "Phân Loại"
        item["field6value"] = phanloai
        item["field6display"] = "1"
        item["field6global"] = "1"
        item["meta1"] = ""
        item["meta2"] = ""
        item["meta3"] = ""
        item["meta4"] = ""
        item["meta5"] = ""
        


        # print('Fetched next page', self.count)
        self.count += 1
        yield item
