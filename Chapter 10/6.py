#Function
def toCaesar(myFile,swipe):
    result = ''
    try:
        file = open(myFile,"r")
        for i in file.read():
            if i=='':
                result+=i
            elif i.islower:
                result+=chr((ord(i)+swipe-97)%26+97)
            else:
                result+=chr((ord(i)+swipe-65)%26+65)
        file.close
    except FileNotFoundError:
        print("File tidak ditemukan")
    else:
        fileEnc = open(myFile+'.encrypt','w')
        fileEnc.write(result)
        fileEnc.close()
        print("File enkripsi:{}.encrypt".format(myFile))

#Input
myFile = input("Nama file yang akan dienkripsi:")
try:
    key=int(input('Input key:'))
except ValueError:
    print("Masukkan angka saja")
toCaesar(myFile,key)
                  
