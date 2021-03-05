# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule

from bs4 import BeautifulSoup
import urllib


class SimpleNextPage(CrawlSpider):
    name = 'SimpleNextPage'
    allowed_domains = ['ruoutaychinhhang.com']
    start_urls = [
        'https://https://ruoutaychinhhang.com/whisky',
    ]


    custom_settings = {

    'LOG_LEVEL': 'INFO',
 
    }

    def parse(self, response):
        print('Current page ', response.url)

        nextpage = response.css('.page-item a::attr(href)').extract()
        nextpagetext = response.css('.pagination-next').extract()

        yield scrapy.Request(nextpage[0], callback=self.parse_next_page)
        return  




    def parse_next_page(self, response):
        print('Fetched next page', response.url)
        return