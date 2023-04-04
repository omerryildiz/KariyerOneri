import spacy
import pathlib
nlp = spacy.load("en_core_web_lg")
#print(nlp.meta["name"])
#print(nlp)
intro = nlp("this tutorial is about Natrural Language Processing in spaCy")
#print(type(intro))

tokenize_intro = [token.text for token in intro]

#print(tokenize_intro)


file_name ="C:/Users/omeryildiz/Desktop/KariyerOneri/text_file/10089434.txt"
intro_doc = nlp(pathlib.Path(file_name).read_text(encoding="utf-8"))
print([token.text for token in intro_doc])