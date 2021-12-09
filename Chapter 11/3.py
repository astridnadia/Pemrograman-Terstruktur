from datetime import * 
def searchlibrary(kode):
    myFile = 'Library'
    pengembalian = datetime.date(datetime.now())
    file = open(myFile,'r')
    for i in file.readlines():
        i = i.split('|')
        if kode == i[0]:
            print('Data Peminjam Buku')
            print('Kode Member :',i[0])
            print('Nama Member :',i[1])
            print('Judul Buku :',i[2])
            print('Tanggal Mulai Peminjaman :',i[3])
            print('Tanggal Maks Peminjaman :',i[4])
            print('Tanggal Pengembalian :',pengembalian)
            terlambat = i[4]-pengembalian
            print('Terlambat : {} hari'.format(terlambat))
            print('Denda : Rp', terlambat*2000)
            result = ''
            break
        else:
            result = 'Data Peminjaman Tidak Ditemukan'
    print(result) 
 
kode = input('Masukkan Kode Member : ')
searchlibrary(kode)
