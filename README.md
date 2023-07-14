# learning-scrapy-framework

###  What is Scrapy?

Scrapy is a free and open-source web-crawling framework written in python.

It was originally designed for web scrapping but can also be used for extracting the data using the APIs or as a general purpose web crawler.

It is currently maintained by Scrapinghub Ltd.

### What is A WebCrawler?

* A web-crawler is also known as a web spider, automatic indexer or simply crawler.

* It is an internet bot that helps in web indexing

* Web crawlers helps in collecting information from a webpage and the links related to them

* It also helps in validating HTML code and hyperlinks.

* They crawl one page at a time until all the pages are indexed.

## How to Install Scrapy?

To install scrapy, simply run the following in the command prompt or in the terminal, or simply you can add the package from the project interpreter too.

`pip install scrapy`


## Project

* [Jessops](/jessops)
    
    * Creating a project: `scrapy startproject jessops`
    * [Spider Code](/jessops/jessops/spiders/jessops_spider.py) 
    * [Item Code](/jessops/jessops/items.py) 
    * [Output Data](/jessops/product_details.json)
    * Run the project: `scrapy crawl jessops_spider -O product_details.json`

* [Fake Plants](/fake_plants)
    
    * Creating a project: `scrapy startproject fake_plants`
    * [Spider Code](/fake_plants/fake_plants/spiders/fake_plant.py)
    * [Output Data](/fake_plants/product_details.json)
    * Run the project: `scrapy crawl fake_plant -O product_details.json`

* [Whisky Shop](/whiskyshop)
    
    * Creating a project: `scrapy startproject whiskyshop`
    * [Spider Code](/whiskyshop/whiskyshop/spiders/whisky_shop.py)
    * [Output Data](/whiskyshop/details.json)
    * Run the project: `scrapy crawl whisky_shop -O details.json`
* [Quotes](/quotes)
    
    * Creating a project: `scrapy startproject quotes`
    * [Spider Code](/quotes/quotes/spiders/quotes_spider.py)
    * [Database Code](/quotes/quotes/database.py)
    * [CSV Output Code](/quotes/items.csv)
    * [JSON Output Code](/quotes/items.json)
    * [XML Output Code](/quotes/items.xml)
    * [DB Output Code](/quotes/myquote.db)
    * Run the project: `scrapy crawl quotes -O items.csv`
* [Worldometer Corona Virus](/worldometer_coronavirus)
    
    * Creating a project: `scrapy startproject worldomerter_coronavirus`
    * [Spider Code](/worldometer_coronavirus/worldometer_coronavirus/spiders/worldometer_coronavirus_spider.py)
    * [Output Data](/worldometer_coronavirus/details.json)
    * Run the project: `scrapy crawl worldometer_coronavirus_spider -O details.json`
* [Amazon](/amazon)
    
    * Creating a project: `scrapy startproject amazon`
    * [Spider Code](/amazon/amazon/spiders/amazon_spider.py)
    * [Output Data](/amazon/details.json)
    * Run the project: `scrapy crawl amazon_spider -O details.json`

