from collections import defaultdict
import pickle


def posting_list():
    return defaultdict(list)


class InvertedIndex:

    def __init__(self):
        self.index = defaultdict(posting_list)
        self.documents = {}
        self.document_frequency = {}
        self.num_documents = 0

    def build(self, dataframe):

        self.num_documents = len(dataframe)

        for doc_id, row in dataframe.iterrows():

            self.documents[doc_id] = {
                "title": row["title"],
                "authors": row["authors"],
                "abstract": row["abstract"],
                "categories": row["categories"],
                "year": row["year"],
            }

            text = " ".join([
                str(row["processed_title"]),
                str(row["processed_abstract"]),
                str(row["processed_authors"]),
                str(row["processed_categories"]),
            ])

            terms = text.split()

            for position, term in enumerate(terms):
                self.index[term][doc_id].append(position)

        self.document_frequency = {
            term: len(postings)
            for term, postings in self.index.items()
        }

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)