# Function
print("-----------------------------------------------------")
def kuadrat(bil):
    hasil = []
    for i in bil:
        hasil = hasil + [i**2]
    return hasil
bil = [2, 4, 5, 6]
print('Bilangan : ', bil)
hasil = kuadrat(bil)
print('Hasil kuadrat dari bilangan adalah : ', hasil)
print("-----------------------------------------------------")
