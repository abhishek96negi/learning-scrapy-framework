import scrapy


class WorldometerCoronavirusSpiderSpider(scrapy.Spider):
    name = 'worldometer_coronavirus_spider'  # spider name
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/coronavirus/'
    ]

    def parse(self, response):
        for country in response.css(".mt_a"):
            country_link = country.xpath('@href').get()
            country_name = country.xpath('text()').get()
            if country_link:
                yield response.follow(url=country_link, callback=self.page2parser, meta={'country_link':  response.urljoin(country_link), "country_name": country_name})

            # yield {
            #     'country_name': country_name,
            #     'country_link': response.urljoin(country_link),  #  f'https://www.worldometers.info/coronavirus/{country_link}',
            #
            # }

            # response.urljoin(country_link)

    def page2parser(self, response):

        active_cases = response.xpath("(//div[@class='maincounter-number'])[1]/span/text()").get()
        deaths_cases = response.xpath("(//div[@class='maincounter-number'])[1]/span/text()").get()
        recovered_cases = response.xpath("(//div[@class='maincounter-number'])[1]/span/text()").get()

        yield {
            'country_name': response.request.meta['country_name'],
            'country_link': response.request.meta['country_link'],  #  f'https://www.worldometers.info/coronavirus/{country_link}',
            'active_cases': active_cases,
            'deaths_cases': deaths_cases,
            'recovered_cases': recovered_cases
        }