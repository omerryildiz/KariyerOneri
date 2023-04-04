import pandas as pd
import numpy as np
import unicodedata
import string

df = pd.read_csv(r'C:\Users\omeryildiz\Desktop\KariyerOneri\UpdatedResumeDataSet.csv', encoding='utf-8')
print(df.head())
df['Resume'] = df['Resume'].apply(lambda x: ''.join(ch for ch in unicodedata.normalize('NFKD', x) if not unicodedata.combining(ch)))
df['Resume'] = df['Resume'].apply(lambda x: ''.join(filter(lambda ch: ch in string.printable, x)))

print(df)
#.at[1,'Resume']