# Program untuk membuat 'diagram' jumlah mahasiswa PTIK UNS
print('============== Program Membuat Diagram Jumlah Mahasiswa =============='+'\n')

LakiLaki = int(input('Berapa jumlah mahasiswa laki-laki di prodi PTIK UNS?'))
Perempuan = int(input('Berapa jumlah mahasiswa perempuan di prodi PTIK UNS?'))

lk = int(LakiLaki/10)
pr = int(Perempuan/10)
print('=============='+'\n')
print('Laki-laki = '+'*' * lk)
print('Perempuan = '+'*' * pr)
