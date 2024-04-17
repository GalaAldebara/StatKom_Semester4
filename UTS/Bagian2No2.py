import numpy as np
def interval_kepercayaan(rata_rata_sampel, simpangan_baku_populasi, ukuran_sampel, tingkat_kepercayaan):
    z = 1.96  
    margin_error = z * (simpangan_baku_populasi / np.sqrt(ukuran_sampel))
    batas_bawah = rata_rata_sampel - margin_error
    batas_atas = rata_rata_sampel + margin_error
    return (batas_bawah, batas_atas)

rata_rata_sampel = 15  
simpangan_baku_populasi = np.sqrt(16)
ukuran_sampel = 25  
tingkat_kepercayaan = 0.95  

interval = interval_kepercayaan(rata_rata_sampel, simpangan_baku_populasi, ukuran_sampel, tingkat_kepercayaan)

print("Rentang nilai rata-rata populasi dari tinggi tanaman dengan tingkat kepercayaan 95%")
print("Rentang nilai rata-rata populasi:", interval)