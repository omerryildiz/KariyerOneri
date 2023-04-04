import PyPDF2
import unicodedata

pdf_file = open('10089434.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Bozuk karakterleri temizle ve metin dosyasına yazdır
with open('temiz_cv.txt', 'w', encoding='utf-8') as text_file:
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        text = page.extractText()
        clean_text = ''.join(c for c in text if unicodedata.category(c)[0] != 'C')
        text_file.write(clean_text)

pdf_file.close()
