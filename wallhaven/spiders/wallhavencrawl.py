# -*- coding: utf-8 -*-
import scrapy
from wallhaven.items import WallhavenItem


class WallhavencrawlSpider(scrapy.Spider):
    name = 'wallhavencrawl'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/latest?page=3']

    def parse(self, response):
        pagenum = response.css('#thumbs  section  header  h2::text').getall()[-1].split('/ ')[-1]
        # 获取总页数 pagenum = 12709
        # pagenum = 2 测试一下
        urls = 'https://wallhaven.cc/latest?page='
        for i in range(2, int(pagenum) + 1):
            yield scrapy.Request(url=urls + str(i), callback=self.parse2)

    def parse2(self, response):
        imgpageurl = response.css('#thumbs  section  ul  li  figure  a::attr(href)').getall()
        # imgpageurl = response.css('#thumbs  section  ul  li  figure').getall()
        for i in imgpageurl:
            # 获取图片的具体页面

            item = WallhavenItem()
            item['imgpageurl'] = i
            # print(i) 测试打印图片页面地址
            yield scrapy.Request(url=i, callback=self.parse3, meta={'item': item})


    def parse3(self, response):
        item = response.meta['item']
        item['imageurl'] = response.css('#wallpaper::attr(src)').get()
        item['imagesize'] = response.css('#showcase-sidebar  div  div.sidebar-content  h3::text').get()
        yield item
