def kalkulator_sederhana_nuNox():
    
    nama = input ("Masukkan Nama : ")
    nim  = input("Masukkan Nim : ")
    print(nama)
    print(nim)

    input_pertama = float(input(" Masukkan Angka Pertama : "))
    input_kedua = float(input(" Masukkan Angka Kedua : "))
    operator = input("Masukkan Operasi Angka (+, -, *, / ): ")

    if operator == "+":
        result = input_pertama + input_kedua
    elif operator == "-":
        result = input_pertama - input_kedua
    elif operator == "*":
        result = input_pertama * input_kedua
    elif operator == "/":
        result = input_pertama / input_kedua
    
    print(f"{input_pertama} {operator} {input_kedua} = {result}")

kalkulator_sederhana_nuNox()