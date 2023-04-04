import csv
import pandas as pd

# CSV dosyasının yolunu belirle
csvDosyasi = r"C:\Users\omeryildiz\Desktop\KariyerOneri\UpdatedResumeDataSet.csv"

# CSV dosyasını oku
veri = pd.read_csv(csvDosyasi)

# Verileri işle
for index, row in veri.iterrows():
    print(row)