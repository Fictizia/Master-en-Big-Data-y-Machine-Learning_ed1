# -*- coding: utf-8 -*-
import scrapy
import selenium
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from scrapy import Request

class Page():
    def parse(self, response):
        print(response.url)
        self.driver.get(response.url)



class FictiziaSpider(scrapy.Spider):
    name = 'fictizia'
    allowed_domains = ['milanuncios.com']
    start_urls = ['http://milanuncios.com/']

    def parse(self, response):
        
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        max_pages = 5

        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")
        options.add_argument("-–disable-web-security")
        options.add_argument("--no-sandbox")

        capabilities = options.to_capabilities()
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', desired_capabilities=capabilities)
        
        master = 'http://milanuncios.com/motor/?pagina='
        current = 1

        while current < max_pages:

            self.driver.get(master + str(current))

            time.sleep(3)
                
            urls = self.driver.find_elements_by_class_name('aditem-detail-title')
                
            for url in urls:
                time.sleep(2)
                #self.driver.get(url.get_attribute('href'))
                page = Page()
                yield Request(url=url.get_attribute('href'),
                              callback=page.parse)
                print('ahora')
                print(urls)

            current += 1

        print(response)
        pass
