from search_engine.preprocessing import preprocess_text


class BooleanSearcher:

    def __init__(self, index):
        self.index = index

    def get_documents(self, term):

        tokens = preprocess_text(term)

        if not tokens:
            return set()

        token = tokens[0]

        if token not in self.index.index:
            return set()

        return set(self.index.index[token].keys())

    def search(self, query):

        query = query.strip()

        if " AND " in query:

            left, right = query.split(" AND ")

            return self.get_documents(left) & self.get_documents(right)

        elif " OR " in query:

            left, right = query.split(" OR ")

            return self.get_documents(left) | self.get_documents(right)

        elif " NOT " in query:

            left, right = query.split(" NOT ")

            return self.get_documents(left) - self.get_documents(right)

        else:

            return self.get_documents(query)