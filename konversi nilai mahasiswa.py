print("===========================================")
nama = input(" Masukkan Nama : ")
nim = input(" Masukkan Nim : ")
print("===========================================")
print(f"Nama Mahasiswa :{nama} Berhasil Terdaftar!")
print(f"Nim Mahasiswa  :{nim} Berhasil Terdaftar")
print("===========================================")

def konversi_nilai_mahasiswa_nunox(nilai_angka):
    while True:
        try:
            if nilai_angka >= 90:
                return "A+"
            elif nilai_angka >= 80:
                return "A"
            elif nilai_angka >= 75:
                return "A-"
            elif nilai_angka >= 72.50:
                return "B+"
            elif nilai_angka >= 70:
                return "B"
            elif nilai_angka >= 67.50:
                return "B-"
            elif nilai_angka >= 65:
                return "B/C"
            elif nilai_angka >= 62.50:
                return "C+"
            elif nilai_angka >= 60:
                return "C"
            elif nilai_angka >= 57:
                return "C-"
            elif nilai_angka >= 55:
                return "D"
            else:
                return "E"
        except KeyboardInterrupt:
            print("error")
        except EOFError:
            print("error")
        except ValueError:
            print("=====")
            print("error")
            print("=====")

while True:
    try:
        nilai_angka = float(input("Masukkan nilai angka mahasiswa: "))
        print("=====================================================") 
        nilai_huruf = konversi_nilai_mahasiswa_nunox(nilai_angka)
        print("Nilai mahasiswa:", nilai_huruf)
        print("======================================================")
    except KeyboardInterrupt:
            print("error")
    except EOFError:
            print("=====")
            print("error")
            print("=====")
    except ValueError:
            print("=====")
            print("error")
            print("=====")
