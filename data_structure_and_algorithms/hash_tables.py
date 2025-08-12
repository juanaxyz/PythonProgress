# basic
'''

hash_table: dict = {}

hash_table["nama"] = "juana"
hash_table["umur"] = 19
hash_table["profesi"] = "mahasiswa"

print(hash_table["nama"])
print("menggunakan loop")
for key, value in hash_table.items():
    print(f"{key} : {value}")
    
del hash_table["umur"]
print("deleted umur")
for key, value in hash_table.items():
    print(f"{key} : {value}")

'''


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def _hashing_func(self,key): #hashing ini untuk menentukan value mau ditaruh di index ke berapa
        return sum(ord(char) for char in key) % self.size
    
    def set(self,key,value):
        index = self._hashing_func(key)
        self.table[index] = (key,value) #gunakan tuple ()
        print(f"[DEBUG] {key} tersimpan di index {index}")
        
    def get(self, key): 
        index = self._hashing_func(key)
        entry = self.table[index]
        if entry and entry[0] == key:
            return entry[1]
        return None
    
    def delete(self,key):
        index = self._hashing_func(key)
        entry = self.table[index]
        if entry and entry[0] == key:
            self.table[index] = None
        return None
    
mahasiswa = HashTable(11)

mahasiswa.set("nama","satya adi")
mahasiswa.set("aman","aku")
print(mahasiswa.get("nama")) # kalau indexnya sama maka akan ditimpa oleh key,value baru ini disebut *collision*
print(mahasiswa.get("aman"))


