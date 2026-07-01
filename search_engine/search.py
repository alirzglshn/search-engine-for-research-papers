from search_engine.tfidf import TFIDFSearcher
from search_engine.snippets import SnippetGenerator


class SearchEngine:

    def __init__(self, index):

        self.index = index
        self.tfidf = TFIDFSearcher(index)
        self.snippets = SnippetGenerator()

    def search(self, query, top_k=10):

        ranked = self.tfidf.search(query, top_k)

        results = []

        for doc_id, score in ranked:

            paper = self.index.documents[doc_id].copy()

            paper["doc_id"] = doc_id
            paper["score"] = score

            paper["snippet"] = self.snippets.generate(
                paper["abstract"],
                query
            )

            results.append(paper)

        return results