import scrapy
from scrapy.http import FormRequest
from ..items import QuotesItem
from scrapy.utils.response import open_in_browser

# scrapping the data without login
# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#
#     # start_urls = [
#     #      'https://quotes.toscrape.com/'
#     # ]
#
#     # pagination
#     page_number = 2
#
#     start_urls = [
#          'https://quotes.toscrape.com/page/1/'
#     ]
#
#     def parse(self, response):
#
#         items = QuotesItem()
#         all_div_quotes = response.css("div.quote")
#         for quote in all_div_quotes:
#
#             title = quote.css("span.text::text").extract()
#             author = quote.css(".author::text").extract()
#             tags = ",".join(quote.css(".tag::text").extract())
#             items['title'] = title
#             items['author'] = author
#             items['tags'] = tags
#
#             yield items
#         # No Pagination
#
#         # next_page = response.css('li.next a::attr(href)').get()
#         # if next_page is not None:
#         #     yield response.follow(next_page, callback=self.parse)
#
#         next_page = f"https://quotes.toscrape.com/page/{QuoteSpider.page_number}/"
#         if QuoteSpider.page_number <= 10:
#             QuoteSpider.page_number += 1
#             yield response.follow(next_page, callback=self.parse)
#
#


# scrapping the data with login

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'crsf_token': token,
            'username': 'admin',
            'password': 'admin'
        },callback=self.start_scrapping)

    def start_scrapping(self, response):
     #   open_in_browser(response) for checking the functionality
        items = QuotesItem()
        all_div_quotes = response.css("div.quote")
        for quote in all_div_quotes:

            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tags = ",".join(quote.css(".tag::text").extract())
            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items