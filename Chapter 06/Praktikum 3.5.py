from operation import *
#a
a = 2
b = 4
c = 6
d = 4
print(a, '+', b, '*', c, '-', d, '=', kurang(jumlah(a, kali(b,c)), d))
#b
a = 4
b = 7
c = 6
d = 9
print('(',a, '+', b,') * (',c, '-', d,')=', kali(jumlah(a,b), kurang(c,d)))
#c
a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print('(',a, '+', b,')/(',c, '+', d,')/(',e, '-', f,')=', bagi(bagi(jumlah(a,b), jumlah(c,d)), kurang(e,f)))
