#Nama   : Ikbal Miftahudin
#NIM    : 2401426
#Kelas  : 1C

# Menghitung total biaya pembuatan dinding
def hitung_biaya_dinding(panjang, lebar, tinggi, biaya_per_m2):
    # Menghitung luas permukaan dinding
    luas_dinding = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)
    
    # Menghitung total biaya
    total_biaya = luas_dinding * biaya_per_m2
    return total_biaya

# Input dimensi bangunan
panjang = float(input("Masukkan panjang bangunan (m): "))
lebar = float(input("Masukkan lebar bangunan (m): "))
tinggi = float(input("Masukkan tinggi bangunan (m): "))

# Biaya per m2
biaya_per_m2 = 520000

# Menghitung total biaya
total_biaya = hitung_biaya_dinding(panjang, lebar, tinggi, biaya_per_m2)

# Menampilkan hasil
print(f"Total biaya yang harus dikeluarkan Pak Abi untuk pembuatan dinding adalah: Rp {total_biaya:.2f}")


