from search_engine.indexer import InvertedIndex

index = InvertedIndex.load("data/indexes/inverted_index.pkl")

print("Vocabulary:", len(index.index))

print()

term = "retriev"

print(term)

print(index.index.get(term, {}))