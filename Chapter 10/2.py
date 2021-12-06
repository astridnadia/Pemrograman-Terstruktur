#Function1
def inputDataMhs(myFile, nim, name, address):
    dataMhs = open(myFile, "a")
    dataMhs.write("{}|{}|{}\n".format(nim, name, address))
    dataMhs.close

#Function2
def viewDataMhs(myFile):
    result = open(myFile, "r")
    for x in result:
        print(x)
    result.close()

#Input lagi
myFile = "DATAMAHASISWA.txt"
answer = "y"
while answer=="y":
    nim = input('\nMasukkan NIM Mahasiswa:')
    name = input("Masukkan Nama Mahasiswa:")
    address = input("Masukkan Alamat Mahasiswa:")
    inputDataMhs(myFile, nim, name, address)
    answer = input('\nApakah ada data yang ingin diinput lagi (y/n) ?')
#Selesai Input
if answer=="n":
    viewDataMhs(myFile)
