#Nama   : Ikbal Miftahudin
#NIM    : 2401426
#Kelas  : 1C

barang_juli = ["T-Shirt", "Blouse", "Kemeja", "Celana Panjang", 
          "Rok", "Baju Renang", "Tas", "Topi", "Sepatu", "Sendal"]

# Memperbarui daftar barang untuk bulan ini
barang_bulan_ini = barang_juli.copy()  
barang_bulan_ini.remove("Baju Renang")   
barang_bulan_ini.append("Gamis")     
barang_bulan_ini.append("Ikat Rambut") 
barang_bulan_ini.append("Kerudung")   

# Menampilkan daftar barang bulan Juli
print("Daftar Barang Jualan Bulan Juli:")
for barang in barang_juli:
    print(f"- {barang}")
print(f"Jumlah jenis barang bulan Juli: {len(barang_juli)}")

# Menampilkan daftar barang bulan ini
print("\nDaftar Barang Jualan Bulan Ini:")
for barang in barang_bulan_ini:
    print(f"- {barang}")
print(f"Jumlah jenis barang bulan ini: {len(barang_bulan_ini)}")
