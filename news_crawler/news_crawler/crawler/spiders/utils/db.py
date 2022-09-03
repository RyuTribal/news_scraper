# -*- coding: utf-8 -*-

"""
Holds the code for database management.
Everything from cache database to storage database should be 
placed in this file
"""

__title__ = "news_crawler"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

import psycopg2
import redis, time
from google.cloud import storage

class CloudBlobStorage(object):
    """
    Object abstracts connection details for google cloud storage
    """
    def __init__(self, creds_path='', bucket='', project=''):
        
        self.client = storage.Client.from_service_account_json(creds_path)
        self.bucket = self.client.get_bucket(bucket)

    def upload_file(self, file_bytes, file_name):
        self.bucket.blob(file_name).upload_from_string(file_bytes, content_type='text/html')



class CacheSQL(object):
    """
    Object abstracts connection details for postgresql
    """

    def __init__(
        self,
        host="localhost",
        database="crawler",
        user="root",
        password="admin",
        port=5432,
    ):
        self.creds = {}
        self.creds["host"] = host
        self.creds["port"] = port
        self.creds["database"] = database
        self.creds["user"] = user
        self.creds["password"] = password

    def connect(self):
        self.conn = psycopg2.connect(**self.creds)
        if not self.table_exists("url_cache"):
            self.create_cache_table()

    def create_cache_table(self):
        cur = self.conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS public.url_cache
                    (
                        id serial NOT NULL,
                        url text COLLATE pg_catalog."default" NOT NULL,
                        scraped timestamp without time zone NOT NULL DEFAULT now(),
                        CONSTRAINT url_cache_pkey PRIMARY KEY (id),
                        CONSTRAINT url_cache_url_key UNIQUE (url)
                    )

                    TABLESPACE pg_default"""
        )
        cur.execute(
            "COMMENT ON TABLE public.url_cache IS 'For storing url''s that have been crawled'"
        )
        self.conn.commit()
        cur.close()

    def table_exists(self, table_str):
        exists = False
        cur = self.conn.cursor()
        try:
            cur.execute(
                "select exists(select relname from pg_class where relname='"
                + table_str
                + "')"
            )
            exists = cur.fetchone()[0]
            print(exists)
        except psycopg2.Error as e:
            print(e)
        cur.close()
        return exists

    def add_url(self, url):
        cur = self.conn.cursor()
        try:
            cur.execute("insert into url_cache(url) values(%s)", [url])
            self.conn.commit()
        except:
            cur.rollback()
            raise Exception('Failed to insert into cache, probably a duplicate url so probably nothing to worry about')
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


class CacheRedis(object):
    """
    Object abstracts connection details for redis
    """

    def __init__(self, host="localhost", port=6379, db=0, password=""):
        self.creds = {}
        self.creds["host"] = host
        self.creds["port"] = port
        self.creds["db"] = db
        self.creds["password"] = password

    def connect(self):
        self.conn = redis.Redis(**self.creds)

    def add_url(self, url):
        self.conn.set(url, time.time())

    def check_url_exists(self, url):
        return self.conn.get(url)

    def close_connection(self):
        pass
