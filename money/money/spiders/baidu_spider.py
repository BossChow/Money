#!/usr/bin/env python
# encoding: utf-8

import scrapy

class BaiduSpider(scrapy.Spider):
    name = "BaiduMovieSpider"

    allowed_domain = ["baidu.com"]

    start_urls = ["http://top.baidu.com/category?c=1&fr=topindex"]

    def parse(self, response):
        for li in response.css('.item-list')[0].xpath('li'):
            #Ranking
            rank = li.xpath('div/span')[0].xpath('text()').extract_first()
            name = li.xpath('div/a')[0].xpath('text()').extract_first()
            url = li.xpath('div/a')[0].xpath('@href').extract_first()

            print "%s %s" % (rank, name)

