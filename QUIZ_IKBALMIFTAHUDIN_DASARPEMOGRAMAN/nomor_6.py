#Nama   : Ikbal Miftahudin
#NIM    : 2401426
#Kelas  : 1C


# Informasi mobil lama
mobil = {
    "Merk": "Honda", 
    "Tipe": "HRV",
    "Tahun": "2018",
    "Warna": "Hitam", 
    "No. Polisi": "D 1234 ABC", 
    "Bensin": "Pertalite", 
    "Transmisi": "Manual"
}

mobil_lama = mobil.copy() 

# Menampilkan informasi mobil lama
print("Informasi Mobil Lama:")
for key, value in mobil.items():
    print(f"{key}: {value}")

print("----------***----------")

# Mengupdate informasi mobil baru berdasarkan inputan
print('Masukan Informasi detail mobil baru :')
mobil["Merk"] = input(" Merk mobil : ")
mobil["Tipe"] = input(" Tipe mobil : ")
mobil["Tahun"] = input(" Tahun mobil : ")
mobil["Warna"] = input(" Warna mobil : ")
mobil["No. Polisi"] = input(" Nomor polisi mobil : ")
mobil["Bensin"] = input("  Bensin mobil : ")
mobil["Transmisi"] = input("  Transmisi mobil : ")

print("---------- *** ----------")

# Menampilkan informasi mobil baru
print("\nInformasi Mobil Baru:")
for key, value in mobil.items():
    print(f"{key}: {value}")