nama = input ("Masukkan Nama : ")
nim  = input("Masukkan Nim :")
tempat_tanggal_lahir = input("Masukkan Tempat, Tanggal, Lahir :")
Asal_Daerah = input("Asal Daerah :")
Asal_Sekolah = input("Asal Sekolah :")
motto_hidup = input("Motto Hidup :")

print(nama)
print(nim)
print(tempat_tanggal_lahir)
print(Asal_Daerah)
print(Asal_Sekolah)
print(motto_hidup)

def menghitung_nilai_tukar_duit(jumlah_rupiah, mata_uang_tujuan):
    nilai_mata_uang = {
        "US Dollar": 0.65,
        "YEN Jepang": 96.56,
        "Ringgit Malaysia": 3.05,
    }

    if mata_uang_tujuan not in nilai_mata_uang:
        raise ValueError(
            "Jangan Typo Bossque wkwk : " + ", ".join(nilai_mata_uang)
        )

    nilai_tukar = nilai_mata_uang[mata_uang_tujuan]
    jumlah_mata_uang_tujuan = jumlah_rupiah / nilai_tukar
    return jumlah_mata_uang_tujuan

if __name__ :
    #__name__ adalah variabel bawaan yang mengevaluasi nama modul atau skrip saat ini.
    jumlah_rupiah = float(input("Masukkan jumlah rupiah yang ingin dikonversikan : "))
    mata_uang_tujuan = input("Masukkan mata uang yang dituju: ")
    jumlah_mata_uang_tujuan = menghitung_nilai_tukar_duit(jumlah_rupiah, mata_uang_tujuan)
    print("CMIIW")
    print("Nilai {} Rupiah ke {} adalah: {} {}".format(jumlah_rupiah, mata_uang_tujuan, jumlah_mata_uang_tujuan, mata_uang_tujuan))