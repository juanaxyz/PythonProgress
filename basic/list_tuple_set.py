'''
#### list, tuple dan set
list -> pop = hapus, append = tambah
tuple -> + immutable, 
set -> tidak terurut, no duplicate, mutable
add untuk menambah
remove dan discard untuk menghapus (remove akan error jika item tidak ditemukan, sedangkan discard tidak)
'''
# list
list1 = [1, 'juana', True, 1.5]

print(list1)
list1.pop(-1)
print(list1)
list1.append(1.5)
print(list1)


# tuple
koordinat = (10, 20)
warna = ("merah", "hijau", "biru", "merah")
info_produk = ("Laptop", 1200.00, 2024)
tuple_baru = koordinat + warna

print(koordinat)    # Output: (10, 20)
print(warna)        # Output: ('merah', 'hijau', 'biru', 'merah')
print(info_produk)  # Output: ('Laptop', 1200.0, 2024)

print(warna.count("merah"))
print(warna.index("biru"))

try:
    warna[0] = "biru"
    print(warna)
except:
    print("tupple tidak bisa diubah")

print(tuple_baru)
print(len(koordinat))


# set
primary_category = {"f&b", "fo", "security"}
# num = {1, 2, 3, 4, 5, 1}  # 1 diabaikan

print(primary_category)
# print(num)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (gabungan)
print(set1.union(set2))         # Output: {1, 2, 3, 4, 5, 6}

# Intersection (irisan)
print(set1.intersection(set2))  # Output: {3, 4}

# Difference (selisih)
# Output: {1, 2} (item di set1 tapi tidak di set2)
print(set1.difference(set2))
# Output: {5, 6} (item di set2 tapi tidak di set1)
print(set2.difference(set1))

# Symmetric Difference (selisih simetris)
# Output: {1, 2, 5, 6} (item yang ada di salah satu set, tapi tidak di keduanya)
print(set1.symmetric_difference(set2))

print("fo" in primary_category)  # cek apakah "fo" ada di primary_category
