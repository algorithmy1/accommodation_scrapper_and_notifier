import scrapy


class SelogerLinksSpyder(scrapy.Spider):
    name = "selogerLinks"

    def start_requests(self):
        urls = [
            'https://static-seloger.com/list.htm?tri=initial&enterprise=0&idtypebien=2,1&div=2238&idtt=2,5&naturebien=1,2,4',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'seLoger-%s.html' % page
        print("---------->", response.body)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)