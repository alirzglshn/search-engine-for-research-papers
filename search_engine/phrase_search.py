from search_engine.preprocessing import preprocess_text


class PhraseSearcher:

    def __init__(self, index):
        self.index = index

    def search(self, phrase):

        terms = preprocess_text(phrase)

        if not terms:
            return set()

        if any(term not in self.index.index for term in terms):
            return set()

        candidate_docs = set(self.index.index[terms[0]].keys())

        for term in terms[1:]:
            candidate_docs &= set(self.index.index[term].keys())

        results = set()

        for doc_id in candidate_docs:

            first_positions = self.index.index[terms[0]][doc_id]

            for pos in first_positions:

                match = True

                for i in range(1, len(terms)):

                    if (pos + i) not in self.index.index[terms[i]][doc_id]:
                        match = False
                        break

                if match:
                    results.add(doc_id)
                    break

        return results