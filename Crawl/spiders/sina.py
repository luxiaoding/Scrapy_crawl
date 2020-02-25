# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Crawl.items import CrawlItem

class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'news.sina.com.cn'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//title/text()').extract()[0]
        return item
