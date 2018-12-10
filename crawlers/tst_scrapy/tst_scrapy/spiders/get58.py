# -*- coding: utf-8 -*-
import scrapy


class Get58Spider(scrapy.Spider):
    name = 'get58'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    def parse(self, response):
        pass
