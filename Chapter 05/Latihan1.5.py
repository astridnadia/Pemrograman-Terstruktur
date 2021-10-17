# Tampilkan identitas karyawan
kodeKaryawan = int(input("Masukkan kode karyawan :"))
namaKaryawan = input("Masukkan nama karyawan :")
golongan = input("Masukkan golongan :")
status = int(input("Masukkan status(ketik '1' jika sudah menikah dan '2' jika belum) :"))
if(status==1):
    jumlahAnak = int(input("Masukkan Jumlah Anak :"))

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

# Tunjangan
totalPotong = gajiPokok*(potongan/100)
if(status==1):
    tunjangan= gajiPokok*(10/100)
    tunjanganAnak= gajiPokok*(5/100)*jumlahAnak
    gajiKotor= gajiPokok + tunjangan + tunjanganAnak
    gajiBersih= gajiKotor-totalPotong
gajiBersih2=gajiPokok-totalPotong

    
# Tampilkan struk rincian gaji
print("=======================================")
print("      STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------")
print("Nama Karyawan             : ",namaKaryawan,"Kode:",kodeKaryawan,")")
print("Golongan                  : ",golongan)
print('Status                    :  ', end='')
if(status==1):
    print('Menikah')
else:
    print('Belum Menikah')
if(status==1):
    print('Jumlah Anak               : ', jumlahAnak)
print("----------------------------------------")
if(status==1):
    print('Tunjangan Istri/Suami     :Rp.', tunjangan)
    print('Tujangan Anak             :Rp.', tunjanganAnak)
    print("---------------------------------------+")
    print('Gaji Kotor                :Rp.', gajiKotor)
print('Potongan(',potongan,'%)          :Rp.', totalPotong)
print("-------------------------------------- -")
if(status==1):
    print('Gaji Bersih               :Rp.',gajiBersih)
else:
    print('Gaji Bersih               :Rp.',gajiBersih2)
    print("====================================")

     
