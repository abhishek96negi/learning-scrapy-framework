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
