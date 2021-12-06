#Function 
def DataMahasiswa(myFile):
    data = open(myFile, "r")
    DataMahasiswa = data.read().splitlines()

#Membuat Tampilan output
    for i in DataMahasiswa:
        x = i.split('|')
        dataMhs = [{'nim': x[0], 'nama': x[1], 'alamat': x[2]}]
        print(dataMhs)
        return dataMhs

myFile = "DATAMAHASISWA.txt"
DataMahasiswa(myFile)
