import scrapy

class BbcSpider(scrapy.Spider):
    name = 'bbc_page'
    allowed_domains = ['www.bbc.com']
    start_urls = ['https://www.bbc.com/news/world-europe-60675599']

    def parse(self, response):
        for page in response.xpath("//article"):
            yield {
                'title': page.xpath("//article/div/h1[@id='main-heading']/text()").get(),
                'description':  page.xpath("//article").extract()
            }

