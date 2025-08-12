'''
harga = [1000, 2000,5000,10000]

nama = ["juana", "Aku", "Muli", "adinata"]

print(list(map(lambda x: x * 0.75, harga)))
sorted = sorted(nama, key=lambda x: len(x))


print(sorted)
'''
# implementation
products = [
    {"name": "Laptop", "price": 12000, "stock": 5},
    {"name": "Mouse", "price": 150, "stock": 20},
    {"name": "Keyboard", "price": 350, "stock": 15},
    {"name": "Monitor", "price": 2500, "stock": 7},
    {"name": "Flashdisk", "price": 120, "stock": 50},
]

# menampilkan barang murah
show_murah = list(filter(lambda x: x["price"] < 1000,products)) #lambda menghasilkan object jadi harus di ubah ke list
# print(product["name"] for product in show_murah)
print(*(n["name"] for n in show_murah))

