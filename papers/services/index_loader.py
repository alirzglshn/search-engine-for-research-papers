"""Loads the pre-built inverted index once per process."""

from functools import lru_cache

from django.conf import settings

from search_engine.indexer import InvertedIndex


@lru_cache(maxsize=1)
def get_index() -> InvertedIndex:
    return InvertedIndex.load(str(settings.SEARCH_INDEX_PATH))