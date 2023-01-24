# -*- coding: utf-8 -*-

"""
Anything natural language related should be abstracted into this file.
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

import re
import math
from os import path, environ

from collections import Counter

from . import settings
import spacy
import sv_core_news_md


def keywords_spacy(text):
    nlp = spacy.load("sv_core_news_md")

    clean_text = re.sub('\n', ' ', text)  # strip newlines

    keywords = []

    stop_words = nlp.Defaults.stop_words

    doc = nlp(clean_text)

    for i in doc.ents:
        if i.lemma_ not in stop_words and (i.label_ != "TME" or i.label_ != "MISC"):
            keywords.append(i.lemma_.lower())

    keywords = list(dict.fromkeys(keywords))

    return keywords
