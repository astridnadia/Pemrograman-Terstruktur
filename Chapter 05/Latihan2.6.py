# Game tebak angka
from random import randint
print("Hai...nama saya Mr.Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
bilTebakan = randint(0,100)
poin = 100
while True:
    jawaban = int(input("Tebakan Anda :"))
    if(jawaban > bilTebakan):
        print("Bilangan tebakan Anda terlalu besar")
        poin-=2
    elif(jawaban < bilTebakan):
        print("Bilangan tebakan Anda terlalu kecil")
        poin-=2
    elif(jawaban == bilTebakan):
        print("Horee...Bilangan tebakan Anda BENAR :)")
        break
print("Score Anda :",poin)
