# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import os.path

domain = ""
class ArticleScraperSpider( CrawlSpider ):
	name = 'article_scraper'
	allowed_domains = [domain]
	ind = 0 
	rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

	def start_requests(self):
		start_urls = ['domain']

		for url in start_urls:
			yield scrapy.Request( url = url , callback = self.parse )


	def parse_items(self, response):

		
		url = response.url
		if "articulo" in url:
			nn = url.split("/")[-1]
			# Path raro... 
			filename = "../../../../data/{}.html".format( nn )
			if os.path.exists(filename):
				self.log("FILE ALREADY EXISTS SPIKING")
				return 

			with open(filename , "wb"  ) as f:
				f.write(response.body)

			self.log("saved file")

     
