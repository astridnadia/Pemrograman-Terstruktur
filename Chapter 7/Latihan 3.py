print("-----------------------------")
print("   PROGRAM HITUNG RATA-RATA  ")
print("-----------------------------")
try:
    while True:
        bil = input("Masukkan bilangan bulat:")
        bilbulat = [int(x) for x in bil]
        total = 0
        for bil in bilbulat:
            total += bil
        average = total/len(bilbulat)
        if bil == float:
            print("Bukan merupakan bilangan bulat")
        repeat = input("Masukkan lagi? (y/n) :")
        if repeat == "y":
            print(end="")
        if repeat == "n":
            print("Rata-rata = ", average)
except ValueError:
    print("Bukan merupakan bilangan bulat")
