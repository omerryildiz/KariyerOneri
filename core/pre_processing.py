import spacy

nlp = spacy.load('en_core_web_lg', disable=['parser', 'ner'])


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    return tokens


def preprocess_text(file_path):
    text = load_file(file_path)
    tokens = tokenize_text(text)
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text


def save_preprocessed_text(preprocessed_text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(preprocessed_text)
