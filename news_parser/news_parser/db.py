# -*- coding: utf-8 -*-

"""
Holds the code for database management.
Everything from cache database to storage database should be 
placed in this file
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"


from elasticsearch import Elasticsearch, ConflictError
from datetime import datetime
import pandas as pd


class ElasticDB(object):
    """
    Object abstracts connection details for elasticsearch
    """

    def __init__(
        self,
        cloud_id=None,
        api_key=None,
        username="",
        password="",
        scheme="http",
        host="localhost",
        port=9200,
        index="news_articles",
    ):

        self.creds = {}
        self.creds["cloud_id"] = cloud_id
        self.creds["api_key"] = api_key
        self.creds["username"] = username
        self.creds["password"] = password
        self.creds["scheme"] = scheme
        self.creds["host"] = host
        self.creds["port"] = port
        self.creds["index"] = index

    def connect(self):
        if self.creds["cloud_id"] and self.creds["api_key"]:
            self.client = Elasticsearch(
                cloud_id=self.creds["cloud_id"],
                api_key=self.creds["api_key"],
            )
        else:
            self.client = Elasticsearch(
                [self.creds["host"]],
                http_auth=(self.creds["username"], self.creds["password"]),
                scheme=self.creds["scheme"],
                port=443,
            )

    def add_document(self, doc):
        try:
            self.client.index(index=self.creds["index"], document=doc)
            return True
        except ConflictError:
            print("\n")
            print(ConflictError.info)
            print("\n")
            return False


