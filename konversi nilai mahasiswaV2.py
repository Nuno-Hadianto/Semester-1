RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

print(BOLD + BLUE +"===========================================" + RESET)
nama = input(BOLD + YELLOW + " Masukkan Nama : " + RESET)
nim = input(BOLD + YELLOW + " Masukkan Nim : " + RESET)
print(BOLD + BLUE + "===========================================" + RESET)
print(BOLD + YELLOW + f"Nama Mahasiswa :{nama} Berhasil Terdaftar!" + RESET)
print(BOLD + YELLOW + f"Nim Mahasiswa  :{nim} Berhasil Terdaftar!" + RESET)
print(BOLD + BLUE + "===========================================" + RESET)

def konversi_nilai_mahasiswa_nunox(nilai_angka):
    while True:
        try:
            if nilai_angka >= 90:
                return BOLD + CYAN + "A+" + RESET
            elif nilai_angka >= 80:
                return BOLD + CYAN + "A" + RESET
            elif nilai_angka >= 75:
                return BOLD + CYAN + "A-" + RESET
            elif nilai_angka >= 72.50:
                return BOLD + CYAN + "B+" + RESET
            elif nilai_angka >= 70:
                return BOLD + CYAN + "B" + RESET
            elif nilai_angka >= 67.50:
                return BOLD + CYAN + "B-" + RESET
            elif nilai_angka >= 65:
                return BOLD + CYAN + "B/C" + RESET
            elif nilai_angka >= 62.50:
                return BOLD + CYAN + "C+" + RESET
            elif nilai_angka >= 60:
                return BOLD + CYAN + "C" + RESET
            elif nilai_angka >= 57:
                return BOLD + CYAN + "C-" + RESET
            elif nilai_angka >= 55:
                return BOLD + CYAN + "D" + RESET
            else:
                return BOLD + CYAN + "E" + RESET
        except KeyboardInterrupt:
            print(BOLD + RED + "error" + RESET)
        except EOFError:
            print(BOLD + RED + "error" + RESET)
        except ValueError:
            print(BOLD + RED + "=====" + RESET)
            print(BOLD + RED + "error" + RESET)
            print(BOLD + RED + "=====" + RESET)

while True:
    try:
        nilai_angka = float(input(BOLD + YELLOW + "Masukkan nilai angka mahasiswa: " + RESET))
        print(BOLD + BLUE + "=====================================================" + RESET) 
        nilai_huruf = konversi_nilai_mahasiswa_nunox(nilai_angka)
        print(BOLD + CYAN + "Nilai mahasiswa:" + RESET, nilai_huruf)
        print(BOLD + BLUE + "======================================================" + RESET)
    except KeyboardInterrupt:
            print(BOLD + RED + "error" + RESET)
    except EOFError:
            print(BOLD + RED + "=====" + RESET)
            print(BOLD + RED + "error" + RESET)
            print(BOLD + RED + "=====" + RESET)
    except ValueError:
            print(BOLD + RED + "=====" + RESET)
            print(BOLD + RED + "error" + RESET)
            print(BOLD + RED + "=====" + RESET)
