'''
dictionary = {key : value}
dapat diakses menggunakan [key] atau method get()
dapat dihapus dengan :
* del : menghapus item
* pop : menghapus dan mereturn value yang dihapus (bisa set return value jika key tidak valid)
* popitem : menghapus item terakhir dan mereturn item sebagai tuple
* clear : menghapus semua item


- mutable
'''

siswa = {
    "nama": "juana",
    "usia": 19,
    "alamat": "Bangli",
    "alive": True
}

# akses value dictionary
print(siswa["nama"])

print(siswa.get("usia"))
# get akan menghasilkan none atau nilai default yang dapat kita tentukan jika key tidak valid
print(siswa.get("jurusan"))
print(siswa.get("jurusan", "key tidak valid"))

# mengubah value
siswa["usia"] = 20
print(siswa)

# menambah item
siswa["jurusan"] = "Teknologi Informasi"

# menghapus key - value
del siswa["nama"]
print(siswa)

deleted = siswa.pop("usia")
print(f"value yang dihapus adalah : {deleted}")
deleted = siswa.pop("usia", "key tidak valid")
print(f"value yang dihapus adalah : {deleted}")

deleted = siswa.popitem()
print(f"item yang dihapus : {deleted}")

# looping dictionary
toko = {
    "tv": 34,
    "kabel": 12,
    "antena": 20,
    "lampu": 100
}

# loop menggunakan key
for key in toko:
    print(key)
print("##### menggunakan keys()")
for key in toko.keys():
    print(key)

# loop menggunakan values
for values in toko.values():
    print(values)

# loop item
for key, value in toko.items():
    print(f"stok {key} adalah {value}")

# copy dictionary
toko_copy = toko.copy()
toko_copy["lampu"] = 50

# update dictionary
# data_tambahan = {
#     "mouse": 5,
#     "tv": 1
# }
# toko_copy.update(data_tambahan)
toko_copy.update({
    "mouse": 5,
    "tv": 1
})

print(f"toko asli : {toko}")
print(f"toko copy : {toko_copy}")
