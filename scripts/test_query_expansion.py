from search_engine.indexer import InvertedIndex
from search_engine.query_expansion import QueryExpander

index = InvertedIndex.load("data/indexes/inverted_index.pkl")

searcher = QueryExpander(index)

while True:

    query = input("\nQuery: ")

    if query.lower() == "exit":
        break

    expanded = searcher.expand_query(query)

    print("\nExpanded Query:")

    print(expanded)

    print()

    results = searcher.search(query)

    if not results:
        print("No results found.")
        continue

    for rank, (doc_id, score) in enumerate(results, start=1):

        print(rank, index.documents[doc_id]["title"])