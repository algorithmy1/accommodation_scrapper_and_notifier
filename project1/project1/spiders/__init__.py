import scrapy


class SelogerLinksSpyder(scrapy.Spider):
    name = "selogerLinks"

    def start_requests(self):
        urls = [
            'https://www.seloger.com/list.htm?projects=1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'seLoger-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)