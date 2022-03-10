import scrapy


class BbcSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['www.bbc.com']
    start_urls = ['http://www.bbc.com/']

    def parse(self, response):
        bbc_link = response.xpath("//a[@class='block-link__overlay-link']/@href").getall()
        yield from response.follow_all(bbc_link, self.parsePage)

    def parsePage(self, response):
        site_url = response.request.url

        title = response.xpath("//article/header/h1/text()").get()

        if "/sport/live/" in site_url:
            title = None#"/sport/live/"

        if "/news/live/" in site_url:
            title = None# "/news/live/"

        if "/future/article/" in site_url:
            title = None#"/future/article/"

        if "/travel/article/" in site_url:
            title = None#"/travel/article/"
            title = response.xpath(
                "//section/div[@class='article-headline__text b-reith-sans-font b-font-weight-300]'/text()").get()

        if "/culture/article/" in site_url:
            title = "/culture/article/"
            title = response.xpath(
                "//section/div[@class='article-headline__text b-reith-sans-font b-font-weight-300]'/text()").get()

        if "/news/av/" in site_url:
            title = "/news/av/"
            title = response.xpath("//article/div/h1/text()").get()

        if "/sport/av/" in site_url:
            title = "/sport/av/"
            title = response.xpath("//article/div/h1/text()").get()

        if "/worklife/article/" in site_url:
            title = "/worklife/article/"

    #    if (title is None) or (title is ""):
    #        title = response.xpath("//article/div/h1/text()").get()


        #description = response.xpath('//article/div[@data-component="text-block"]/div/p/text()').getall()

    #    if (description is None) or (description is ""):
    #        response.xpath('//article/div[@aria-live="polite"]/div').getall()

        for page in response.xpath("//article"):
            yield {
                'url': site_url,
                'title': title,
                #'description': description
            }

