mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print("==============================================================")
print("NIM".ljust(10),"NAMA MAHASISWA".ljust(19),"TGL LAHIR".ljust(8),"TEMPAT LAHIR".ljust(8))
print("-------------------------------------------------------------")
for data in mhs :
    dataList = data.split(":")
    nim = dataList[0]
    nama = dataList[1]
    tglLahir = dataList[2]
    dataTglLahir = tglLahir.split('-')
    formatbaruTglLahir = "{0}/{1}/{2}".format(dataTglLahir[0],dataTglLahir[1],dataTglLahir[2])
    tempatLahir = dataList[3]
    print(nim.ljust(10), nama.ljust(19), formatbaruTglLahir.ljust(8), tempatLahir.ljust(8))

print("==============================================================")
