import os

dizin = 'C:\\Users\\omeryildiz\\Desktop\\cvler\\data\\data\\INFORMATION-TECHNOLOGY'

os.chmod(dizin, 0o777)

for kok_dizin, alt_dizinler, dosyalar in os.walk(dizin):
    for alt_dizin in alt_dizinler:
        os.chmod(os.path.join(kok_dizin, alt_dizin), 0o777)
    for dosya in dosyalar:
        os.chmod(os.path.join(kok_dizin, dosya), 0o777)
