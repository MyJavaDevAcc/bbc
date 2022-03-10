import scrapy


class BbcPageSpider(scrapy.Spider):
    name = 'bbc_page'
    allowed_domains = ['www.bbc.com']
    start_urls = ['https://www.bbc.com/news/world-europe-60675599']

    def parse(self, response):
        for page in response.xpath("//article"):
            yield {
                'title': page.xpath("//article/header/h1/text()").get(),
                'description':  page.xpath('//article/div[@data-component="text-block"]/div/p/text()').getall()
            }
