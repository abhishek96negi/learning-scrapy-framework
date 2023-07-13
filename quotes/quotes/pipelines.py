# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/csv files

# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3
# import mysql.connector
# import pymongo


# class QuotesPipeline:
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         # for sqlite
#
#         self.conn = sqlite3.connect('myquote.db')
#         # for mysql
#
#         # self.conn = mysql.connector.connect(
#         #     host='localhost',
#         #     user='root',
#         #     password='root',
#         #     database='myquote',
#         #
#         # )
#
#         # for mongodb
#         # self.conn = pymongo.MongoClient(
#         #     'localhost',
#         #     27017
#         # )
#
#         self.curr = self.conn.cursor()
#
#
#         # create database in mongo
#     #    self.db = self.conn['myqotes']
#
#
#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
#         self.curr.execute("""create table quotes_tb(
#                         title text,
#                         author text,
#                         tag text)""")
#
#         # create a collection/table in mongo
#
#         # self.collection = self.db['quotes_tb']
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         print("PIPELINE :", item['title'])
#         return item
#
#     def store_db(self, item):
#         # for sqlite
#         self.curr.execute("""insert into quotes_tb values(?,?,?)""", (
#             item['title'][0], item['author'][0], item['tags']
#         ))
#
#         # for mysql
#         # self.curr.execute("""insert into quotes_tb values(%,%,%)""", (
#         #     item['title'][0], item['author'][0], item['tags']
#         # ))
#         self.conn.commit()
#
#         # storing the data in mongo
#         # self.collection.insert(dict(item))
#


class QuotesPipeline:
    def process_item(self, item, spider):
        return item