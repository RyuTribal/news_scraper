# -*- coding: utf-8 -*-

"""
Holds the code for database management.
Everything from cache database to storage database should be 
placed in this file
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection


class ElasticDB(object):
    """
    Object abstracts connection details for elasticsearch
    """

    def __init__(
        self, username="", password="", sha_cert="", url="", index="news_articles"
    ):

        self.client = Elasticsearch(
            url,
            connection_class=RequestsHttpConnection,
            http_auth=(username, password),
            use_ssl=True,
            verify_certs=False,
        )

        self.index = index

    def add_document(self, doc):
        try:
            self.client.index(index=self.index, document=doc)
            return True
        except Exception:
            print("Could not save")
            return False
