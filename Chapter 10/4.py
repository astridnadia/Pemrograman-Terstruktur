#MENCARI DATA MAHASISWA
myFile = open("DATAMAHASISWA.txt","r")
data = myFile.readlines()
i=0
baru = []
for lists in data:
    dataMhs = str(data[i])
    dataMhs = dataMhs.split('|')
    baru.append(dataMhs)
    i+=1

#Membuat Tampilan Output
find = input("Masukkan NIM yang dicari:")
hasil = False
a=0


for x in baru:
    if find in baru[a]:
        b=0
        for lists in baru:
            if find==baru[b][0]:
                print('Data Mahasiswa')
                print('NIM\t:'+baru[b][0])
                print('Nama\t:'+baru[b][1])
                print('Alamat\t:'+baru[b][2])
                hasil=True
                break
            else:
                b+=1
    a+=1
if hasil==False:
    print("Data Mahasiswa tersebut tidak ditemukan")
                
                
