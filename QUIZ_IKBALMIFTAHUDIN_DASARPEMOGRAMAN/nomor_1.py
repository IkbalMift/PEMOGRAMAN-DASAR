#Nama   : Ikbal Miftahudin
#NIM    : 2401426
#Kelas  : 1C

#Daftar Nilai Siswa-Siswa
nilai = {90, 86, 57, 59, 95, 77, 67, 94, 82, 86}

# Input nomor urut siswa
no_urut = int(input("Masukkan nomor urut siswa (1-10): "))

# Memeriksa input dan menampilkan nilai
if 1 <= no_urut <= 10:
    print(f"Nilai siswa dengan nomor urut {no_urut} adalah: {nilai[no_urut - 1]}")
else:
    print("Nomor urut tidak valid. Silakan masukkan antara 1 hingga 10.")

