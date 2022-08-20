import news_crawler

from news_crawler import CacheSQL, CloudBlobStorage

import os

pg_creds = dict(
    host= os.environ['POSTGRES_HOST'],
    port= os.environ['POSTGRES_PORT'],
    user= os.environ['POSTGRES_USER'],
    password= os.environ['POSTGRES_PASSWORD']
)

# Requires a json key from Google Cloud
path = os.path.abspath('storage_creds.json')


pg = CacheSQL(**pg_creds)

blob_storage = CloudBlobStorage(creds_path=path, bucket=os.environ['BUCKET'])

news_crawler.run(os.environ['START_URL'], cache=pg, blob_storage=blob_storage)