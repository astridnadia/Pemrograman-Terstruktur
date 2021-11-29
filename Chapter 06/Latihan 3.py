import math

#KOMBINASI
def C(n, r):
    f = math.factorial
    kombinasi = f(n)//f(r)//f(n-r)
    print('C(', n,',', r,'):', kombinasi)
C(5,3)

#PERMUTASI
def P(n,r):
    f = math.factorial
    permutasi = f(n-r)//1
    print('P(', n,',',r,'):', permutasi)
P(10,7)
