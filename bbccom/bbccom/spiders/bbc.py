import scrapy

class BbcSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['www.bbc.com']
    start_urls = ['http://www.bbc.com/']

    def parse(self, response):
        bbclink = response.xpath("//a[@class='block-link__overlay-link']/@href").getall()
        yield from response.follow_all(bbclink, self.parsePage)

    def parsePage(self, response):
        for page in response.xpath("//article"):
            yield {

                'title': page.xpath("//article/div/h1[@id='main-heading']/text()").get(),
                'description':  page.xpath("//article").extract()
            }
