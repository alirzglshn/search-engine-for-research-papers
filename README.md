# Research Paper Search Engine

## Overview

This project is a simple Information Retrieval search engine.

The system indexes research paper metadata from the arXiv dataset (from Cornell University) and provides multiple search methods over the indexed collection.

The project was implemented from scratch without using dedicated search libraries.

## Dataset

Dataset:

- arXiv Metadata Dataset

Number of indexed papers:

- 10,000

Indexed fields:

- Title
- Abstract
- Authors
- Categories

Stored metadata:

- Title
- Authors
- Abstract
- Categories
- Publication Year

## Features

Implemented features:

- Text preprocessing
- Tokenization
- Stopword removal
- Porter stemming
- Inverted index construction
- TF-IDF ranking
- Keyword search
- Boolean search
- Phrase search
- Wildcard search
- Query expansion
- Result snippet generation

## Project Structure

```
research-search-paper-engine/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── indexes/
│
├── scripts/
│
├── search_engine/
│
├── requirements.txt
└── README.md
```

## Search Engine Components

### Preprocessing

The preprocessing pipeline performs:

- Lowercasing
- Tokenization
- Stopword removal
- Porter stemming

Example:

Original:

```
Information Retrieval Systems are used for document search.
```

Processed:

```
inform retriev system use document search
```

### Inverted Index

The inverted index stores:

- vocabulary
- document IDs
- term positions
- document frequency

Term positions are stored to support phrase search.

### TF-IDF

Documents are ranked using TF-IDF scores based on query terms.

### Keyword Search

Retrieves and ranks documents containing the query terms.

### Boolean Search

Supports:

- AND
- OR
- NOT

Example:

```
retrieval AND neural
```

### Phrase Search

Supports exact phrase matching.

Example:

```
"information retrieval"
```

### Wildcard Search

Supports prefix wildcard queries.

Example:

```
retriev*
```

### Query Expansion

Query expansion uses a small manually defined synonym dictionary.

Example:

```
retrieval

↓

retrieval search index
```

### Snippet Generation

Each result includes a short excerpt from the abstract containing the matched query term when available.

## Running the Project

### 1. Create a virtual environment

```
python -m venv irvenv
```

### 2. Activate it

Windows

```
irvenv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Place the dataset

```
data/raw/arxiv-metadata-oai-snapshot.json
```

### 5. Generate the sample dataset

```
python -m scripts.sample_dataset
```

### 6. Preprocess the dataset

```
python -m scripts.preprocess
```

### 7. Build the inverted index

```
python -m scripts.build_index
```

## Technologies

- Python
- Pandas
- NumPy
- NLTK

## Current Status

Completed:

- Dataset extraction
- Preprocessing
- Inverted index
- TF-IDF ranking
- Keyword search
- Boolean search
- Phrase search
- Wildcard search
- Query expansion
- Snippet generation

The web interface and evaluation components have not yet been implemented.

Developed by Alireza Golshan & Homayoon Mohammadi Fard
