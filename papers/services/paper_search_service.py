from search_engine.boolean_search import BooleanSearcher
from search_engine.phrase_search import PhraseSearcher
from search_engine.query_expansion import QueryExpander
from search_engine.snippets import SnippetGenerator
from search_engine.tfidf import TFIDFSearcher
from search_engine.wildcard_search import WildcardSearcher

from papers.services.index_loader import get_index
from papers.services.query_router import SearchMode, detect_search_mode


def search_papers(raw_query: str) -> list[dict]:
    """Run the query through the appropriate search mode.

    Returns a list of paper dicts sorted by relevance, each containing
    a TF-IDF score and a generated snippet. The full ranked result set is
    returned; the view is responsible for paginating it.
    """

    index = get_index()
    mode = detect_search_mode(raw_query)
    max_results = index.num_documents

    if mode == SearchMode.PHRASE:
        phrase = raw_query.strip().strip('"')
        doc_ids = PhraseSearcher(index).search(phrase)
        ranked = _rank_doc_ids(index, doc_ids, phrase)

    elif mode == SearchMode.BOOLEAN:
        doc_ids = BooleanSearcher(index).search(raw_query)
        ranked = _rank_doc_ids(index, doc_ids, raw_query)

    elif mode == SearchMode.WILDCARD:
        ranked = WildcardSearcher(index).search(raw_query, top_k=max_results)

    else:
        ranked = QueryExpander(index).search(raw_query, top_k=max_results)

    return _build_results(index, ranked, raw_query)


def _rank_doc_ids(index, doc_ids: set, query: str) -> list[tuple]:
    """Score an unranked set of doc_ids by re-running TF-IDF on the query.

    Used for Boolean and phrase search, which return matching documents
    without a relevance score. Only doc_ids present in the original
    matching set are kept.
    """

    if not doc_ids:
        return []

    all_scores = TFIDFSearcher(index).search(query, top_k=index.num_documents)

    ranked = [
        (doc_id, score)
        for doc_id, score in all_scores
        if doc_id in doc_ids
    ]

    scored_ids = {doc_id for doc_id, _ in ranked}
    unscored = [(doc_id, 0.0) for doc_id in doc_ids if doc_id not in scored_ids]

    return ranked + unscored


def _build_results(index, ranked: list[tuple], query: str) -> list[dict]:
    """Turn (doc_id, score) pairs into displayable paper dicts."""

    snippet_generator = SnippetGenerator()
    results = []

    for doc_id, score in ranked:
        paper = index.documents[doc_id].copy()
        paper["doc_id"] = doc_id
        paper["score"] = score
        paper["snippet"] = snippet_generator.generate(paper["abstract"], query)
        results.append(paper)

    return results