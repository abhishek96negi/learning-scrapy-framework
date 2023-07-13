# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Extracted data ==> Temporary containers (items) --> Storing in database.

# We are going to learning how to put that extracted data in containers called items.

# Now why exactly do we need to put them in containers? Because we have already extracted the data. Can't we just put them in some kind of database? The answer is yes. You can. But there might be a few problems when you are storing the data directly in the database when you are working on big/multiple projects.

# Scrapy spiders can return the extracted data as Python dictionaries which we have already been doing right with our quotes project. But the problem with Python dictionaries is that it lacks structure. It is easy to make a typo in a field name or return inconsistent data, especially in a larger project with many spiders.

# So it's always a good idea to move the scraped data to temporary location called containers and then store them inside the database. So these temporary containers are called as items.

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

