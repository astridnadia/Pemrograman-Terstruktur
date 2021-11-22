#1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('a =', a)
print('b =', b)
#2
a.insert(3, 10)
b.insert(2, 15)
print('a =', a)
print('b =', b)
#3
a.append(4)
b.append(8)
print('a =', a)
print('b =', b)
#5
a.sort()
b.sort()
print('a =', a)
print('b =', b)
#6
c = a[:8]
d = b[2:10]
print('c =', c)
print('d =', d)
e = []
n = 0
for n in range(len(c)):
    indeks = c[n] + d[n]
    e = e + [indeks]
print('e =', e)
#7
Tuple = tuple(e)
print('e =', Tuple)
#8
nilaiMinimal =  min(Tuple)
nilaiMaksimal = max(Tuple)
jumlah = sum(Tuple)
print('Nilai minimalnya :', nilaiMinimal)
print('Nilai maksimalnya :', nilaiMaksimal)
print('Jumlah seluruh elemen e :', jumlah)
#9
myString = "python adalah bahasa pemograman yang menyenangkan"
print(myString)
#10
susunan = set(myString)
print('Karakter huruf penyusun string tsb adalah :', susunan)
#11
List = list(susunan)
print('Himpunan karakter yang diperolah adalah :', sorted(List))
