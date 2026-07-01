class SnippetGenerator:

    def __init__(self, window=40):
        self.window = window

    def generate(self, text, query):

        if not text:
            return ""

        text_lower = text.lower()

        query_terms = query.lower().split()

        for term in query_terms:

            position = text_lower.find(term)

            if position != -1:

                start = max(0, position - self.window)
                end = min(len(text), position + len(term) + self.window)

                snippet = text[start:end]

                if start > 0:
                    snippet = "... " + snippet

                if end < len(text):
                    snippet += " ..."

                return snippet

        return text[:2 * self.window] + "..."