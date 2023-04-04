import os
import PyPDF2
import unicodedata

# Klasör yolunu belirleyin
folder_path = "C:/Users/omeryildiz/Desktop/cvler/data/data/INFORMATION-TECHNOLOGY/"

# Tüm PDF dosyalarını alın
pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

# Her PDF dosyasını açın, temizleyin ve .txt dosyası olarak kaydedin
for pdf_file in pdf_files:
    # PDF dosyasını açın
    with open(os.path.join(folder_path, pdf_file), 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Bozuk karakterleri temizleyin ve yeni sayfaları oluşturun
        clean_pages = []
        for i in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(i)
            text = page.extractText()
            clean_text = ''.join(c for c in text if unicodedata.category(c)[0] != 'C')
            page.mergePage(clean_text)
            clean_pages.append(page)

        # Yeni PDF dosyası oluşturun ve temizlenmiş sayfaları yazın
        pdf_writer = PyPDF2.PdfFileWriter()
        for page in clean_pages:
            pdf_writer.addPage(page)

        # Temizlenmiş PDF dosyasını kaydedin
        with open(os.path.join(folder_path, pdf_file[:-4] + '.txt'), 'w', encoding='utf-8') as txt_file:
            txt_file.write(clean_text)
