#Function
def decCaesar(myFile, kry):
    result=''
    try:
        file = open(myFile,"r")
        for i in file.read():
            if i=='':
                result+=i
            elif i.islower():
                hasil+=chr((ord(i)-key-97)%26+97)
            else:
                hasil+=chr((ord(i)-key-65)%26+65)
        file.close()
    except FileNotFoundError:
        print("File tidak dapat ditemukan")
    else:
        fileDec=open(myFile+'.decrypt','w')
        fileDec.write(result)
        fileDec.close()
        print('File dekripsi :{}.decrypt'.format(myFile))

#Input
myFile=input("Nama file yang akan didekripsi:")
try:
    key = int(input("Inputkey:"))
except ValueError:
    print("Masukkan angka saja")
decCaesar(myFile, key)
        
    
