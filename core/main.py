import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')



pdf_file = open(r'C:\Users\omeryildiz\Desktop\KariyerOneri\10089434.pdf', mode='rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
content = ""

for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    content += page.extractText()

pdf_file.close()
#print(content)
print('*******************************************************************')
# Metin verilerini token'lar halinde ayırın
tokens = word_tokenize(content)
# Stop words'leri kaldırın"
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token.lower() not in stop_words]
#print(tokens)
print('*******************************************************************')
# Noktalama işaretlerini kaldırın
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
print('*******************************************************************')
# Kelimeleri köklerine indirin
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in stripped]
print(stemmed)