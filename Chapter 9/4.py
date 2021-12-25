import random

#Function
def shuffleString(r,n) :
    result = []
    i = 0
    while i < n :
        acak = ''.join(random.sample(r,len(r)))
        if (acak not in result) :
            result += [acak]
            i += 1
    print(result)

shuffleString('aku',6)
