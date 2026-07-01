import re
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


def preprocess_text(text: str) -> list[str]:
    if not isinstance(text, str):
        return []

    text = text.lower()

    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)

    
    tokens = re.findall(r"[a-zA-Z]+", text)

    tokens = [
        stemmer.stem(token)
        for token in tokens
        if token not in stop_words
    ]

    return tokens