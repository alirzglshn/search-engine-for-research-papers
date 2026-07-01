from search_engine.preprocessing import preprocess_text
from search_engine.tfidf import TFIDFSearcher


class WildcardSearcher:

    def __init__(self, index):
        self.index = index
        self.tfidf = TFIDFSearcher(index)

    def expand(self, wildcard):

        if not wildcard.endswith("*"):
            return []

        prefix = preprocess_text(wildcard[:-1])

        if not prefix:
            return []

        prefix = prefix[0]

        matches = []

        for term in self.index.index.keys():

            if term.startswith(prefix):
                matches.append(term)

        return sorted(matches)

    def search(self, wildcard, top_k=10):

        terms = self.expand(wildcard)

        if not terms:
            return []

        query = " ".join(terms)

        return self.tfidf.search(query, top_k)