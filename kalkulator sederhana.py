def kalkulator_sederhana_nuNox():
    while True:
        try:
            print("============================================")
            nama = input ("Masukkan Nama : ")
            nim  = input("Masukkan Nim : ")
            print("============================================")
            print(f"Nama Mahasiswa : {nama} Berhasil Terdaftar!")
            print(f"Nim Mahasiswa  : {nim} Berhasil Terdaftar!")
            print("=============================================")

            input_pertama = float(input(" Masukkan Angka Pertama : "))
            print("=================================================")
            input_kedua = float(input(" Masukkan Angka Kedua : "))
            print("==================================================")
            operator = input("Masukkan Operasi Angka (+, -, *, / ): ")
            print("===================================================")

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
        
            print(f"{input_pertama} {operator} {input_kedua} = {result}")
        
        except KeyboardInterrupt:
            print(" [error][Ngulang dari awal]")
        except EOFError:
            print(" [error][Ngulang dari awal]")
        except ValueError:
            print(" [error][Ngulang dari awal]")
        except UnboundLocalError:
            print("[Ngulang dari awal]")

kalkulator_sederhana_nuNox()