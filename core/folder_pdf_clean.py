import os
import unicodedata
from pdfminer.high_level import extract_text

# Kaynak dizini ve hedef dizini ayarlanır
source_dir = "C:/Users/omeryildiz/Desktop/cvler/data/data/INFORMATION-TECHNOLOGY/"
target_dir = "C:/Users/omeryildiz/Desktop/KariyerOneri/text_file"

# Kaynak dizinindeki tüm pdf dosyaları alınır
pdf_files = [f for f in os.listdir(source_dir) if f.endswith('.pdf')]

# Her pdf dosyası için döngü oluşturulur
for pdf_file in pdf_files:
    # Pdf dosyasının tam yolu
    pdf_path = os.path.join(source_dir, pdf_file)
    # Pdf dosyasından metin çıkarılır
    text = extract_text(pdf_path)
    # Bozuk karakterleri temizle
    clean_text = ''.join(c for c in text if unicodedata.category(c)[0] != 'C')
    # Hedef dizine kaydedilir
    target_file = os.path.splitext(pdf_file)[0] + '.txt'
    target_path = os.path.join(target_dir, target_file)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(clean_text)
