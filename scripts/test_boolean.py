from search_engine.boolean_search import BooleanSearcher
from search_engine.indexer import InvertedIndex

index = InvertedIndex.load("data/indexes/inverted_index.pkl")

searcher = BooleanSearcher(index)

while True:

    query = input("\nBoolean Query: ")

    if query.lower() == "exit":
        break

    results = searcher.search(query)

    print(f"\nFound {len(results)} documents.\n")

    for doc_id in list(results)[:10]:

        print(index.documents[doc_id]["title"])