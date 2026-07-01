from search_engine.indexer import InvertedIndex
from search_engine.phrase_search import PhraseSearcher

index = InvertedIndex.load("data/indexes/inverted_index.pkl")

searcher = PhraseSearcher(index)

while True:

    phrase = input("\nPhrase: ")

    if phrase.lower() == "exit":
        break

    results = searcher.search(phrase)

    print(f"\nFound {len(results)} documents.\n")

    for doc_id in list(results)[:10]:
        print(index.documents[doc_id]["title"])