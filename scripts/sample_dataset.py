import json
import pandas as pd
from pathlib import Path
from tqdm import tqdm

RAW_DATA = Path("data/raw/arxiv-metadata-oai-snapshot.json")
OUTPUT = Path("data/processed/papers.csv")

MAX_PAPERS = 10_000

papers = []

with open(RAW_DATA, "r", encoding="utf-8") as file:
    for i, line in enumerate(tqdm(file, total=MAX_PAPERS)):
        if i >= MAX_PAPERS:
            break

        paper = json.loads(line)

        papers.append({
            "id": paper.get("id", ""),
            "title": paper.get("title", ""),
            "authors": paper.get("authors", ""),
            "abstract": paper.get("abstract", ""),
            "categories": paper.get("categories", ""),
            "year": paper.get("update_date", "")[:4]
        })

df = pd.DataFrame(papers)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)

print(f"Saved {len(df)} papers to {OUTPUT}")