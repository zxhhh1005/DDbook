import scrapy
from ..items import DDBOOKItem

class DDBOOKSpider(scrapy.Spider):
    name = 'ddbook'
    allowed_domains = ['dangdang.com']
    base_url = 'http://dangdang.com/'
    start_urls = ['http://category.dangdang.com/cp01.01.03.00.00.00.html']


    def parse(self, response):

        books = response.xpath('//ul[@class="bigimg"]/li')
        i = 0
        for book in books:
            item = DDBOOKItem()
            
            item['b_name'] = book.xpath('./a[@class="pic"]/@title').extract()

            if len(book.xpath('./p[@class="detail"]/text()')) > 0:
                item['b_info'] = book.xpath('./p[@class="detail"]/text()').extract() 
            else:
                item['b_info'] = ['无图书简介信息']

            item['b_pic'] = response.xpath('//ul[@class="bigimg"]/li[@ddt-pit="1"]//img/@src|//ul[@class="bigimg"]/li/a[@dd_name = "单品图片"]/img/@data-original')[i].extract()
           
            if len(book.xpath('./p/span[1]/a[1]/@title')) > 0:
                item['w_name'] = book.xpath('./p/span[1]/a[1]/@title').extract()
            else:
                item['w_name'] = ['无作者信息']

            if len(book.xpath('./p/span[3]/a/@title')) > 0:
                item['p_name'] = book.xpath('./p/span[3]/a/@title').extract() 
            else:
                item['p_name'] = ['无出版社信息']

            if len(book.xpath('./p[5]/span[2]/text()')) > 0:
                item['p_time'] = book.xpath('./p[5]/span[2]/text()').extract()
            else:
                item['p_time'] = ['无出版时间信息']


            item['s_price'] = book.xpath('./p/span[@class="search_now_price"]/text()').extract()

            if len(book.xpath('./p/span[@class="search_pre_price"]/text()')) > 0:
                item['pre_price'] = book.xpath('./p/span[@class="search_pre_price"]/text()').extract()
            else:
                item['pre_price'] = ['无旧价信息']

            if len(book.xpath('./p/span[@class="search_discount"]/text()')) > 0:
                item['disc'] = book.xpath('./p/span[@class="search_discount"]/text()').extract() 
            else:
                item['disc'] = ['无折扣信息']


            item['url'] = book.xpath('./p[@class="name"]/a/@href').extract()[0]
            i = i+1
            yield scrapy.Request(item['url'],meta={'item':item},callback=self.detail_parse)
            

        pageNum = 4
        for page in range(2,pageNum):
            page = f'http://category.dangdang.com/pg{page}-cp01.01.03.00.00.00.html'
            
            yield scrapy.Request(page,callback=self.parse)
    
    def detail_parse(self,response):

            item = response.meta['item']

            if len(response.xpath('//*[@id="detail_describe"]/ul/li[5]/text()')) > 0:
                item['ISBN'] = response.xpath('//*[@id="detail_describe"]/ul/li[5]/text()').extract() 
            else:
                item['ISBN'] = ['该商品为套装，无ISBN信息']
            return item
                    