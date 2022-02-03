import scrapy
import re
class post(scrapy.Item):
    ID = scrapy.Field()
    Toan = scrapy.Field()
    NguVan = scrapy.Field()
    LichSu = scrapy.Field()
    DiaLy = scrapy.Field()
    GDCD = scrapy.Field()
    NgoaiNgu = scrapy.Field()
    VatLy = scrapy.Field()
    HoaHoc = scrapy.Field()
    SinhHoc = scrapy.Field()
def clean(string):
    return re.sub('\s+', ' ', string)
class CrawlingThptqgSpider(scrapy.Spider):
    name = 'thptqg'
    def start_requests(self):
        allow_domainss = 'https://diemthi.vnexpress.net/index/detail/id/'
        links = list(map(lambda x: allow_domainss + str(x), list(range(6603249,6603249+100000))))
        for url in links:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        item = post()
        items = response.xpath('//*[@id="warpper"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td//text()').extract()
        item['ID'] = clean(response.xpath('//*[@id="warpper"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/h2/strong//text()').extract_first())
        for i in range(0, len(items)-1, 2):
            subject = clean(items[i])
            score = clean(items[i+1])
            if 'Toán' in subject:
                item['Toan'] = score
            elif 'Ngữ văn' in subject:
                item['NguVan'] = score
            elif 'Lịch sử' in subject:
                item['LichSu'] = score
            elif 'Địa lý' in subject:
                item['DiaLy'] = score
            elif 'Giáo dục công dân' in subject:
                item['GDCD'] = score
            elif 'Ngoại ngữ' in subject:
                item['NgoaiNgu'] = score
            elif 'Vật lý' in subject:
                item['VatLy'] = score
            elif 'Hóa học' in subject:
                item['HoaHoc'] = score
            elif 'Sinh học' in subject:
                item['SinhHoc'] = score
        yield item



