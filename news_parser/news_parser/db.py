# -*- coding: utf-8 -*-

"""
Holds the code for database management.
Everything from cache database to storage database should be 
placed in this file
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"


from webbrowser import get
from elasticsearch import Elasticsearch, ConflictError
import json
from datetime import datetime, time, date
import locale
import dateutil.parser
from .urls import get_domain


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

        locale.setlocale(locale.LC_TIME, "sv_SE")

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

    def add_document(self, **kwargs):
        kwargs['publish_date'] = self.fix_date(kwargs['publish_date'])
        final_data = json.dumps(kwargs, indent=2, ensure_ascii=False, cls=CustomEncoder)
        self.client.index(index="news_"+self.get_appname(kwargs["url"]), body=final_data)
        return True

    def fix_date(self, date):
        try:
            return datetime.strptime(date, '%A %d %B %Y')
        except:
            pass
        date = dateutil.parser.parse(date)
        
        return date
    
    def get_appname(self, url):
        domain = get_domain(url)
        splitted_url = domain.split('.')
        if len(splitted_url) >= 3:
            # www.aftonbladet.se gives aftonbladet
            return splitted_url[1]
        else:
            # metromode.se gives metromode
            return splitted_url[0]


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        if isinstance(obj, set):
            return list(obj)
        return super(CustomEncoder, self).default(obj)