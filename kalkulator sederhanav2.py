# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

print(RED + "" + RESET)
print(BOLD + "" + RESET)
print(BOLD + "" + RESET)
print(BOLD + "" + RESET)
print(BOLD + "" + RESET)

def kalkulator_sederhana_nuNox():
    while True:
        try:
            print(BOLD + BLUE +"============================================" + RESET)
            nama = input (BOLD + YELLOW +"Masukkan Nama : " + RESET)
            nim  = input(BOLD + YELLOW +"Masukkan Nim : " + RESET)
            print(BOLD + BLUE +"============================================" + RESET)
            print(BOLD + YELLOW + f"Nama Mahasiswa : {nama} Berhasil Terdaftar!" + RESET)
            print(BOLD + YELLOW + f"Nim Mahasiswa  : {nim} Berhasil Terdaftar!" + RESET)
            print(BOLD + BLUE + "=============================================" + RESET)

            input_pertama = float(input(BOLD + YELLOW + " Masukkan Angka Pertama : " + RESET))
            print(BOLD + BLUE + "=================================================" + RESET)
            input_kedua = float(input(BOLD + YELLOW + " Masukkan Angka Kedua : " + RESET))
            print(BOLD + BLUE + "==================================================" + RESET)
            operator = input(BOLD + YELLOW + "Masukkan Operasi Angka (+, -, *, / ): " + RESET)
            print(BOLD + BLUE + "===================================================" + RESET)

            if operator == "+":
                result = input_pertama + input_kedua
            elif operator == "-":
                result = input_pertama - input_kedua
            elif operator == "*":
                result = input_pertama * input_kedua
            elif operator == "/":
                result = input_pertama / input_kedua
            else:
                print("[Salah input]")
        
            print(BOLD + CYAN + f"{input_pertama} {operator} {input_kedua} = {result}" + RESET)
        
        except KeyboardInterrupt:
            print(BOLD + RED + " [error][Ngulang dari awal]" + RESET)
        except EOFError:
            print(BOLD + RED + " [error][Ngulang dari awal]" + RESET)
        except ValueError:
            print(BOLD + RED + " [error][Ngulang dari awal]" + RESET)
        except UnboundLocalError:
            print(BOLD + RED + "[Ngulang dari awal]" + RESET)

kalkulator_sederhana_nuNox()