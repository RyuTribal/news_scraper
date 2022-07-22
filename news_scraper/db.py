# -*- coding: utf-8 -*-

"""
Holds the code for database management.
Everything from cache database to storage database should be 
placed in this file
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from elasticsearch import Elasticsearch, RequestsHttpConnection, ConflictError
import psycopg2


class ElasticDB(object):
    """
    Object abstracts connection details for elasticsearch
    """

    def __init__(
        self, username="", password="", sha_cert="", url="", index="scraped_news"
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
        except ConflictError:
            print("\n")
            print(ConflictError.info)
            print("\n")
            return False

class CacheSQL(object):
    """
    Object abstracts connection details for postgresql
    """
    def __init__(self, host='localhost', database='crawler', user="root", password='admin'):
        self.conn =  psycopg2.connect(
            host=host, database=database, user=user, password=password
        )
        if not self.table_exists("url_cache"):
            self.create_cache_table()



            
    def create_cache_table(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS public.url_cache
                    (
                        id serial NOT NULL,
                        url text COLLATE pg_catalog."default" NOT NULL,
                        scraped timestamp without time zone NOT NULL DEFAULT now(),
                        CONSTRAINT url_cache_pkey PRIMARY KEY (id),
                        CONSTRAINT url_cache_url_key UNIQUE (url)
                    )

                    TABLESPACE pg_default""")
        cur.execute("ALTER TABLE IF EXISTS public.url_cache OWNER to root")
        cur.execute("COMMENT ON TABLE public.url_cache IS 'For storing url''s that have been crawled'")
        self.conn.commit()
        cur.close()

    def table_exists(self, table_str):
        exists = False
        try:
            cur = self.conn.cursor()
            cur.execute("select exists(select relname from pg_class where relname='" + table_str + "')")
            exists = cur.fetchone()[0]
            print(exists)
            cur.close()
        except psycopg2.Error as e:
            print(e)
        return exists

    def add_url(self, url):
        cur = self.conn.cursor()
        cur.execute("insert into url_cache(url) values(%s)", [url])
        self.conn.commit()
        cur.close()

    
    def check_url_exists(self, url):
        cur = self.conn.cursor()
        cur.execute("SELECT from url_cache WHERE url=%s", [url])
        doesExist = cur.fetchone() is not None
        cur.close()

        return doesExist

    def close_connection(self):
        if not self.conn.closed:
            self.conn.close()
