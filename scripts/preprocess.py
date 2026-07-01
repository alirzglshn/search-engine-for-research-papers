import pandas as pd

from search_engine.preprocessing import preprocess_text

INPUT = "data/processed/papers.csv"
OUTPUT = "data/processed/papers_preprocessed.csv"

df = pd.read_csv(INPUT)

df["processed_title"] = df["title"].fillna("").apply(
    lambda text: " ".join(preprocess_text(text))
)

df["processed_abstract"] = df["abstract"].fillna("").apply(
    lambda text: " ".join(preprocess_text(text))
)

df["processed_authors"] = df["authors"].fillna("").apply(
    lambda text: " ".join(preprocess_text(text))
)

df["processed_categories"] = df["categories"].fillna("").apply(
    lambda text: " ".join(preprocess_text(text))
)

df.to_csv(OUTPUT, index=False)

print(f"Saved {len(df)} papers to {OUTPUT}")