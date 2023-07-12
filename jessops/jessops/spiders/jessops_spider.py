import scrapy
from ..items import JessopsItem
from scrapy.loader import ItemLoader


class JessopsSpiderSpider(scrapy.Spider):
    name = 'jessops_spider'
    allowed_domains = ['jessops.com/drones']
    start_urls = [
        'https://www.jessops.com/drones/'
    ]

    def parse(self, response):
        for product in response.css('div.f-grid.prod-row'):
            # ---------------- using without items container --------------------

            # yield {
            #     'Image': product.css('img::attr(src)').get(),
            #     'URL': product.css('a::attr(href)').get(),
            #     'Image': product.css('a::text').getall()[1],
            #     'Description': ",".join(product.css('ul.f-list.j-list').css('li::text').getall()),
            #     'Price': product.css('p.price.larger::text').get()
            # }
            # ---------------------- using with item container  ----------------------
            # item = JessopsItem()
            # item['product_image'] = product.css('img::attr(src)').get()
            # item['product_url'] = product.css('a::attr(href)').get()
            # item['product_name'] = product.css('a::text').getall()[1]
            # item['product_description'] = ",".join(product.css('ul.f-list.j-list').css('li::text').getall())
            # item['product_price'] = product.css('p.price.larger::text').get()
            #
            # yield item

            # -------------------- using item loader ----------------------

            # Create an ItemLoader and specify the item class
            l = ItemLoader(item=JessopsItem(), selector=product)

            # Use add_css and add_xpath methods to load data into the item
            l.add_css('product_image', 'img::attr(src)')
            l.add_css('product_url', 'a::attr(href)')
            l.add_css('product_name', 'h4::text')
            l.add_css('product_description', 'ul.f-list.j-list li::text')
            l.add_css('product_price', 'p.price.larger::text')

            # Yield the loaded item
            yield l.load_item()
