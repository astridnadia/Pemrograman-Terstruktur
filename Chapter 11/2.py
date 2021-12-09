from datetime import*
#function
def BorrowBook(code, name, title):
    date = datetime.date(datetime.now())
    returningdate = date + timedelta(days=7)
    inputList = [code,name,title,str(date),str(returningdate)]
    myFile = 'LIBRARY'
    file = open(myFile,'a')
    file.write('|'.join(inputList))
    file.write('\n')
    file.close()
again = 'y'
while again == 'y':
    code = input("Masukkan Kode Member:")
    name = input("Masukkan Nama :")
    title = input("Masukkan Judul Buku Yang Dipunjam:")
    BorrowBook(code,name,title)
    again = input("Ulangi kembali (y/n)")
