import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data = pd.read_csv("pop1.csv")

plt.figure(figsize=(8, 6))
plt.boxplot(data['height'], vert=False)
plt.title('Boxplot Tinggi')
plt.xlabel('Tinggi (cm)')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data['height'], bins=100)
plt.title('Histogram Tinggi')
plt.xlabel('Tinggi (cm)')
plt.ylabel('Frekuensi')
plt.show()

x = 175
mean_tinggi = 170.035
simpangan_baku_tinggi = 11.232
z_score = (x - mean_tinggi) / simpangan_baku_tinggi
print("Nilai z-score untuk tinggi 175cm:", round(z_score, 2))

peluang_lebih_dari_175 = 1 - norm.cdf(z_score)
print("Peluang orang dengan tinggi lebih dari 175cm:", round(peluang_lebih_dari_175, 3))
