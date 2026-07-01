import math

from search_engine.preprocessing import preprocess_text


class TFIDFSearcher:

    def __init__(self, index):
        self.index = index

    def search(self, query, top_k=10):

        query_terms = preprocess_text(query)

        scores = {}

        N = self.index.num_documents

        for term in query_terms:

            if term not in self.index.index:
                continue

            postings = self.index.index[term]

            df = self.index.document_frequency[term]

            idf = math.log(N / df)

            for doc_id, positions in postings.items():

                tf = len(positions)

                score = tf * idf


                scores[doc_id] = scores.get(doc_id, 0) + score

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]