import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
            #'http://quotes.toscrape.com/page/1/',
            #'http://quotes.toscrape.com/page/2/',
            'http://getcertifiedgetahead.com/index.php/security/security-acronyms/',
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        for item in response.css('article p'):
            a = item.css('strong::text').extract_first()
            if a is not None:
                yield {
                    'acronym': a,
                    'term': item.css('::text')[1].extract()[1:],
                }