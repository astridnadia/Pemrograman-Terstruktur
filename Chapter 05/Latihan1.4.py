# Tampilkan identitas karyawan
kodeKaryawan = int(input("Masukkan kode karyawan :"))
namaKaryawan = input("Masukkan nama karyawan :")
golongan = input("Masukkan golongan :")

# Golongan
if(golongan == "A"):
    gajiPokok = 10000000
    potongan = 2.5
elif(golongan == "B"):
    gajiPokok = 8500000
    potongan = 2.0
elif(golongan == "C"):
    gajiPokok = 7000000
    potongan = 1.5
elif(golongan == "D"):
    gajiPokok = 5500000
    potongan = 1.0
else:
    golongan = False
    print("Golongan tidak ditemukan")

# Tampilkan struk rincian gaji
if(golongan != False):
    print("=======================================")
    print("      STRUK RINCIAN GAJI KARYAWAN")
    print("---------------------------------------")
    print("Nama Karyawan              : ",namaKaryawan,"Kode:",kodeKaryawan,")")
    print("Golongan                   : ",golongan)
    print("---------------------------------------")
    potonganGaji = int(gajiPokok*potongan/100)
    gajiBersih = gajiPokok - potonganGaji
    print("Gaji pokok                 : ",gajiPokok)
    print("Potongan (",potongan,"% )         : ",potonganGaji)
    print("---------------------------------------")
    print("Gaji Bersih                : ", gajiBersih)
     
