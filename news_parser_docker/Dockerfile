FROM python

RUN pip uninstall news-crawler

RUN pip install -i https://eiop-pypiserver-xf5bumghuq-lz.a.run.app/simple/ news-crawler

COPY main.py /main.py

COPY storage_creds.json /storage_creds.json

CMD exec python main.py

# CMD exec /bin/bash

