import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_currency(value):
    return value.replace('£', '').strip()


def remove_extra_spaces(value):
    return ",".join([x.strip() for x in value.strip().split('\n')])


def product_url_modification(value):
    return f'www.jessops.com{value}'


class JessopsItem(scrapy.Item):
    # Define the fields for your item here
    # Use input processors to preprocess the data and output processors to extract the first value

    # Define the fields for your item
    product_image = scrapy.Field(output_processor=TakeFirst())
    product_url = scrapy.Field(
        input_processor=MapCompose(product_url_modification),
        output_processor=TakeFirst()
    )
    product_name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )
    product_description = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_extra_spaces),
        output_processor=TakeFirst()
    )
    product_price = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_currency),
        output_processor=TakeFirst()
    )
