from random import randint
n = 0
while True:
    bil = randint(0, 10)
    print(bil)
    n += 1
    if bil == 5:
        break
print('Jumlah Perulangan :',n)
