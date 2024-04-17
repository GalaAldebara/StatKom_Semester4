from scipy.stats import norm

x = 204
mean = 200
std_dev = 20
z_score = (x - mean) / std_dev

peluang = norm.cdf(z_score)

print("Peluang bahwa 100 pria memiliki kolesterol di bawah 204 mg/dl:", peluang)

