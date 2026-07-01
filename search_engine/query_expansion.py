from search_engine.tfidf import TFIDFSearcher
from search_engine.preprocessing import preprocess_text


class QueryExpander:

    def __init__(self, index):

        self.searcher = TFIDFSearcher(index)

        self.synonyms = {

            "ai": [
                "artifici",
                "intellig"
            ],

            "nlp": [
                "natur",
                "languag",
                "process"
            ],

            "cv": [
                "comput",
                "vision"
            ],

            "retriev": [
                "search",
                "index"
            ],

            "graph": [
                "network"
            ],

            "neural": [
                "deep"
            ],

            "bert": [
                "transform"
            ],

            "transform": [
                "attent"
            ]
        }

    def expand_query(self, query):

        terms = preprocess_text(query)

        expanded = []

        for term in terms:

            expanded.append(term)

            if term in self.synonyms:
                expanded.extend(self.synonyms[term])

        return " ".join(expanded)

    def search(self, query, top_k=10):

        expanded_query = self.expand_query(query)

        return self.searcher.search(expanded_query, top_k)