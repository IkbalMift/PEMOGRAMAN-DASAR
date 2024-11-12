#Nama   : Ikbal Miftahudin
#NIM    : 2401426
#Kelas  : 1C

#Jarak Running Track dalam Meter
panjang_track   = 80
lebar_track     = 32
putaran         = 9

#Keliling Running Track dalam Kilometer
keliling_track  = ((2 * panjang_track) + (2 * lebar_track)) / 1000 #diubah jdi centimeter
total_jarak     = keliling_track * putaran

print(f"Total Jarak yang Ditempuh oleh Bu Rinda adalah {total_jarak} km") 



