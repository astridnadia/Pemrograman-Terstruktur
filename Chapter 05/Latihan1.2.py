bhsindo = int(input("Masukkan nilai Bahasa Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mtk = int(input("Masukkan nilai Matematika : "))

if(bhsindo >= 0) and (bhsindo <= 100) and (ipa >= 0) and (ipa <= 100) and (mtk >= 0) and (mtk <=100):
    if(bhsindo >= 60) and (ipa >= 60) and (mtk > 70):
        print("LULUS")
    else:
        print("TIDAK LULUS")    
else:
    print("Maaf ada yang tidak valid")
