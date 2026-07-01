import pandas as pd

from search_engine.indexer import InvertedIndex

INPUT = "data/processed/papers_preprocessed.csv"
OUTPUT = "data/indexes/inverted_index.pkl"

df = pd.read_csv(INPUT)

index = InvertedIndex()
index.build(df)
index.save(OUTPUT)

print("Documents:", index.num_documents)
print("Vocabulary:", len(index.index))
print("Index saved.")