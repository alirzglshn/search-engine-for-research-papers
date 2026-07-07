from enum import Enum


class SearchMode(Enum):
    PHRASE = "phrase"
    BOOLEAN = "boolean"
    WILDCARD = "wildcard"
    EXPANSION = "expansion"


BOOLEAN_OPERATORS = (" AND ", " OR ", " NOT ")


def detect_search_mode(query: str) -> SearchMode:
    stripped = query.strip()

    if stripped.startswith('"') and stripped.endswith('"') and len(stripped) > 1:
        return SearchMode.PHRASE

    if any(operator in stripped for operator in BOOLEAN_OPERATORS):
        return SearchMode.BOOLEAN

    if stripped.endswith("*"):
        return SearchMode.WILDCARD

    return SearchMode.EXPANSION