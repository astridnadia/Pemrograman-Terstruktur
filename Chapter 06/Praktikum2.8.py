#FUNCTION
def luasSegitiga(a, t):
    luas = a * t / 2
    return luas
alas = 10
tinggi = 20
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luasSegitiga(alas, tinggi))
alas2 = 15
tinggi2 = 45
print('Luas segitiga dg alas ', alas2,
      ' dan tinggi ', tinggi2,
      ' adalah ', luasSegitiga(alas2, tinggi2))
def total(bil1, bil2):
    tot = bil1 + bil2
    return tot
bil1 = luasSegitiga(alas, tinggi)
bil2 = luasSegitiga(alas2, tinggi2)
print('total luas kedua segitiga tersebut = ', total(bil1, bil2))
