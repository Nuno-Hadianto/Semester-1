import json

# Membuat data dalam format dictionary
data = {
    "nama": "nuno",
    "nim": 2309116081
}

# Menulis data JSON ke file "datauser.json"
with open("datauser.json", "w") as dataUser:
    json.dump(data, dataUser)

# Membaca data JSON dari file "datauser.json"
with open("datauser.json", "r") as read_it:
    loaded_data = json.load(read_it)

# Menampilkan data yang telah dibaca
print(loaded_data)
print("NIM:", loaded_data["nim"])

# ------------------------------------------------------------
# txt = "Contoh"

# # Write text data to a text file
# with open("example.txt", "w") as txtfile:
#     txtfile.write(txt)

with open("example.txt", "r") as txtfile:
    baca = txtfile.read()

print(baca)