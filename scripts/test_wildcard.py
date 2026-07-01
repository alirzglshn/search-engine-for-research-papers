from search_engine.indexer import InvertedIndex
from search_engine.wildcard_search import WildcardSearcher

index = InvertedIndex.load("data/indexes/inverted_index.pkl")

searcher = WildcardSearcher(index)

while True:

    query = input("\nWildcard: ")

    if query.lower() == "exit":
        break

    expanded = searcher.expand(query)

    print("\nMatching terms:")

    print(expanded)

    print("\nResults:\n")

    results = searcher.search(query)

    if not results:
        print("No results found.")
        continue

    for rank, (doc_id, score) in enumerate(results, start=1):

        print(rank, index.documents[doc_id]["title"])