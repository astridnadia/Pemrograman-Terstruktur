#Function menampilkan rerata
def rerataHarga():
    harga = list(buah.values())
    total = 0
    banyak = 0
    for i in harga:
        total += i
        banyak += 1
    rerata = total/banyak
    return rerata
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' :6500}
print('Rata-rata harga satuannya adalah:', rerataHarga())
