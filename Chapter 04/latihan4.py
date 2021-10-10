# Variable Assignment
jarakPertama = 125
kecepatanPertama = 62
jarakKedua = 256
kecepatanKedua = 70
waktuBerangkat = 06.00
waktuIstirahat = 0.45

# Operasi Penghitungan
pukulSampai = waktuBerangkat+waktuIstirahat+jarakPertama//kecepatanPertama+jarakKedua//kecepatanPertama

# Tampilkan Hasil
print('Pak Amir sampai di kota tujuan pada pukul ' + str(pukulSampai))
