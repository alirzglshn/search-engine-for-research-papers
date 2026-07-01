from search_engine.indexer import InvertedIndex
from search_engine.search import SearchEngine

index = InvertedIndex.load("data/indexes/inverted_index.pkl")

engine = SearchEngine(index)

print("Research Paper Search Engine")
print("Type 'exit' to quit.\n")

while True:

    query = input("Search: ").strip()

    if query.lower() == "exit":
        break

    results = engine.search(query)

    print()

    if not results:
        print("No results found.\n")
        continue

    for i, paper in enumerate(results, start=1):

        print(f"{i}. {paper['title']}")
        print(f"   Authors: {paper['authors']}")
        print(f"   Year: {paper['year']}")
        print(f"   Score: {paper['score']:.4f}")
        print(f"   Snippet: {paper['snippet']}")
        print()
    