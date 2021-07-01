import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


def start_requests(self):
    for url in self.start_urls:
        yield self.make_requests_from_url(url)
def make_requests_from_url(self, url):
    return Request(url, dont_filter=True)


class MoonSpider(scrapy.Spider):



    name = "MoonSpider"
    allowed_domains = ['www.moonboard.com']

    start_urls = ['https://www.moonboard.com/Dashboard/Index']

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': 'Isotoma2viridis3',
                                                   'username': 'U-zef'},
                                         callback=self.scrape_pages)

    def scrape_pages(self, response):
        open_in_browser(response)
