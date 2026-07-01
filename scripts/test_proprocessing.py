from search_engine.preprocessing import preprocess_text

text = "Information Retrieval Systems are used for document searching."

tokens = preprocess_text(text)

print(tokens)