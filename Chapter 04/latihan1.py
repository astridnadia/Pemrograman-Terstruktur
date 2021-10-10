# Variable assignment
JamMulai = 6
MenitMulai = 00
print('Mobil mulai disewa pada pukul 06:00')

JamSelesai = 23
MenitSelesai = 50
print('Mobil dikembalikan pada pukukl 23:50')

# Operasi penghitungan
JamSewa = JamSelesai - JamMulai
MenitSewa = MenitSelesai - MenitMulai

LamaSewa = JamSewa + MenitSewa / 60
TotalSewa = int(LamaSewa)

TotalBiaya = 200000 + (10000*(TotalSewa - 12))

# Tampilkan hasil
print('Biaya yang perlu dibayarkan untuk rental mobil adalah : ' + str(TotalBiaya))
