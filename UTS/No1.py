import pandas as pd
import numpy as np

data = pd.read_csv("pop1.csv")

print(data.head())

tinggi = data['height']
mean_tinggi = np.mean(tinggi)
varians_tinggi = np.var(tinggi)
simpangan_baku_tinggi = np.sqrt(varians_tinggi)
print("Mean tinggi:", mean_tinggi)
print("Varians tinggi:", varians_tinggi)
print("Simpangan baku tinggi:", simpangan_baku_tinggi)

Q1 = np.percentile(tinggi, 25)
Q2 = np.percentile(tinggi, 50)
Q3 = np.percentile(tinggi, 75)
print("Q1:", Q1)
print("Q2 (Median):", Q2)
print("Q3:", Q3)

IQR = Q3 - Q1
batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR
outliers = data[(tinggi < batas_bawah) | (tinggi > batas_atas)]
jumlah_outliers = len(outliers)
print("Jumlah outliers:", jumlah_outliers)

hasil = {
    "Mean Tinggi": [mean_tinggi],
    "Varians Tinggi": [varians_tinggi],
    "Simpangan Baku Tinggi": [simpangan_baku_tinggi],
    "Q1": [Q1],
    "Q2 (Median)": [Q2],
    "Q3": [Q3],
    "Jumlah Outliers": [jumlah_outliers]
}

df_hasil = pd.DataFrame(hasil)
df_hasil.to_excel("hasil_statistik.xlsx", index=False)
