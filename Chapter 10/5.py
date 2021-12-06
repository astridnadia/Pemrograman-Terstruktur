#Buka notepad pada direktori
myFile ="BILANGAN.txt"
data =open(myFile,"r")


#Menghilangkan angka sebelum split
for i in data:
    i =i.split('|')
    hasil =int(i[0])+ int(i[1])
    print(hasil)
data.close
