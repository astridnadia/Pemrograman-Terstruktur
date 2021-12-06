#Function
def read(myFile):
    bilangan = open(myFile, "r")
    genap = 0
    ganjil = 0
    for data in bilangan:
        if int(data)%2==0:
            genap = genap+1
        else:
            ganjil = ganjil+1
    bilangan.close()
    result = {"genap" : genap, "ganjil" : ganjil}
    return result

myFile = "databilangan.txt"
print('Banyak bilangan genap: ',read(myFile).get("genap"))
print('Banyak bilangan ganjil: ',read(myFile).get("ganjil"))
