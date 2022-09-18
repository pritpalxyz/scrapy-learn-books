import scrapy
from learn_scraping.items import LearnScrapingItem

class BooksCrawlSpider(scrapy.Spider):
    name = 'books_crawl'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for href in response.xpath("//ul[@class='nav nav-list']/li/ul//a/@href").extract():
            href = response.urljoin(href)
            yield scrapy.Request(href, callback=self.parse_books)

    def parse_books(self, response):
        for href in response.xpath("//article[@class='product_pod']/h3/a/@href").extract():
            href = response.urljoin(href)
            yield scrapy.Request(href, callback=self.parse_info)

    def parse_info(self, response):
        item = LearnScrapingItem()
        item['title'] = response.xpath("//h1/text()").extract()
        item['price'] = response.xpath("//div[@class='col-sm-6 product_main']/p[@class='price_color']/text()").extract()
        item['rating'] = response.xpath("//div[@class='col-sm-6 product_main']//p[contains(@class, 'star-rating')]/@class").extract()
        item['image_url'] = response.urljoin(response.xpath("//div[@id='product_gallery']//img/@src").extract()[0])
        item['product_description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").extract()
        item['upc'] = response.xpath("//th[contains(text(), 'UPC')]/following-sibling::td/text()").extract()
        item['direct_url'] = response.url
        item['no_of_reviews'] = response.xpath("//th[contains(text(), 'Number of reviews')]/following-sibling::td/text()").extract()
        yield item
