input("Masukkan nama file:")
try:
    while True:
        file = open("d:/dataMhs.txt", "a")
        data = input("Data yang mau ditambahkan:")
        file.write(data)
        file.close()
        repeat = input("Mau lagi? (y/n) :")
        if repeat == "n":
            break
except FileNotFoundError:
    print("Tidak dapat menemukan file")
