print("\n=== 4. Fungsi ===")
import math

def lingkaran(r):
    luas = math.pi * r * r
    keliling = 2 * math.pi * r
    return luas, keliling

jari_jari = 7
luas, keliling = lingkaran(jari_jari)
print(f"Luas lingkaran dengan r={jari_jari}: {luas:.2f}")
print(f"Keliling lingkaran dengan r={jari_jari}: {keliling:.2f}")