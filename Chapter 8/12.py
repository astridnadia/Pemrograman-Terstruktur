#Function
print('-----------------------------------')
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def myData(x):
    print('Data buah : ')
    for n, i in x.items():
        print('- {0} (Harga Rp {1} / kg)'.format(n, i))
def buy(beli, kg):
    price = buah.get(beli)
    total = price * kg
    return total
while True:
    print('        Menu : ')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Hapus data buah')
    print('D. Keluar')
    jawab = None
    while jawab not in('A', 'B', 'C', 'D'):
        jawab = str(input('\nPilihan menu: '))
        if (jawab == "A"):
            tambah = str(input('\nMasukan nama buah : '))
            if tambah in buah.keys():
                print('Nama buah tersebut sudah ada dalam data')
            else:
                while True:
                    try:
                        hargaTambah = int(input('Masukan harga satuan : '))
                    except ValueError:
                        print('Input angka saja !')
                        continue
                    else:
                        break
                    buah[tambah] = hargaTambah
                    print('{0} (Harga Rp {1} ditambahkan)'.format(tambah, hargaTambah))
                    print('')
                    myData(buah)
        elif(jawab == "B"):
            myData(buah)
            total = 0
            selesai = False
            while not selesai:
                while True:
                    namaBuah = str(input('\nBuah yang akan dibeli : '))
                    if namaBuah not in buah.keys():
                        print('Buah tidak ada')
                        continue
                    else:
                        break
                while True:
                    try:
                        banyak = float(input('Berapa kg : '))
                    except ValueError:
                        print('Input angka saja !')
                        continue
                    else:
                        break
                total = total + buy(namaBuah, banyak)
                jawab = None
                while jawab not in("y", "n"):
                    jawab = str(input('Beli lagi (y/n)? : '))
                    if(jawab == "y"):
                        selesai = False
                        print('')
                    elif(jawab == "n"):
                        selesai = True
                    else:
                        print('Masukan pilihan')
            print('-----------------------------------')
            print('Total harga : Rp {0}'.format(total))
            print('')
            break
        elif(jawab == "C"):
            myData(buah)
            hapus = str(input('Masukan nama buah yang akan dihapus : '))
            if hapus in buah.keys():
                del buah[hapus]
                print('Buah {0} telah dihapus'.format(hapus))
                print('')
                myData(buah)
        elif(jawab == "D"):
            exit()
