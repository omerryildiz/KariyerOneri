import PyPDF2
import unicodedata
import spacy
import pathlib

nlp = spacy.load("en_core_web_lg")
pdf_file = open('10089434.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

page = pdf_reader.getPage(0)
text = page.extractText()

# Bozuk karakterleri temizle
clean_text = ''.join(c for c in text if unicodedata.category(c)[0] != 'C')

print(clean_text)
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

clean_text_pages = []

for page in pdf_reader.pages:
    text = page.extractText()
    # Bozuk karakterleri temizle
    clean_text = ''.join(c for c in text if unicodedata.category(c)[0] != 'C')
    clean_text_pages.append(clean_text)

pdf_file.close()
nlp_clean_text=nlp(clean_text_pages)
print([token.text for token in nlp_clean_text])
# Temizlenmiş metinleri yazdır
# for i, text in enumerate(clean_text_pages):
  
#     print(f"Page {i+1}: {text}")




#print(nlp.meta["name"])
#print(nlp)
intro = nlp("this tutorial is about Natrural Language Processing in spaCy")
#print(type(intro))

tokenize_intro = [token.text for token in intro]

#print(tokenize_intro)


file_name ="linkedlncv.pdf"
intro_doc = nlp(pathlib.Path(file_name).read_text(encoding="utf-16"))
print([token.text for token in intro_doc])