import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
   # allowed_domains = ['https://www.amazon.in/']
    start_urls = [
        'https://www.amazon.in/s?k=iphone+13&ref=nb_sb_noss'
    ]

    def parse(self, response):
        # items = AmazonItem()
        for product_detail in response.css('div.s-result-item'):
            product_name = product_detail.css('.a-color-base.a-text-normal').css('::text').extract()
            product_star = product_detail.css('.a-declarative .a-declarative .aok-align-bottom').css('::text').extract()
            product_price = product_detail.css('.a-price-whole').css('::text').extract()
            product_image_link = product_detail.css('.s-image::attr(src)').extract()
            #   items['product_star'] = product_name
            #   items['product_price'] = product_star
            ##   items['product_price'] = product_price
            #  items['product_image_link'] = product_image_link
            yield {
                'product_name': product_name[0] if product_name else None,
                'product_star': product_star[0] if product_star else None,
                'product_price': product_price[0] if product_price else None,
                'product_image_link': product_image_link[0] if product_image_link else None
            }

        next_page = response.css('.a-last a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
