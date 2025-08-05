'''
hash table dengan handle collision

'''

class hashTable:
    def __init__(self,size: int):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash_function(self,key):
        return sum(ord(c) for c in key ) % self.size
    
    def set(self,key,value):
        #table = [
            # [(k,v),()], = index 0 
            # [],   = index 1
            # []    = index 2
        # ]
        index = self._hash_function(key)
        for i,(k,v) in enumerate(self.table[index]): #cek setiap item di index tersebut
            # cek key apakah sudah ada atau belum jika ada maka update value
            if k == key:
                self.table[index][i] = (key,value)
                return
            
            # kondisi ketika key belum ada
        self.table[index].append((key,value))
    
    def get(self, key):
        index = self._hash_function(key)
        for k,v in self.table[index]:
            if k == key:
                print(f"{key} : {v}")
                return v
        print(f"key : {key} tidak ditemukan")
        return None
    
    def delete(self, key):
        index = self._hash_function(key)
        for i,(k,v) in self.table[index]:
            if k == key:
                del self.table[index][i]
                return
        return None
        
    def displayTable(self):        
        index = 0
        for index in range(self.size):
            if self.table[index]:
                # print(self.table[index])
                for k,v in self.table[index]:
                    print(f"index ke {index} => key = : {k}, value : {v}")
            else:
                print(f"index ke {index} kosong")
    
    def keys(self):
        res = []
        for index in self.table:
            # print(index) #output [('nama', 'filosofi teras'), ('aman', 'dump')]
            for k,_ in index:
                res.append(k)
        
        return res
    def values(self):
        res = []
        for index in self.table:
            for _,v in index:
                res.append(v)
        return res
    
    def items(self):
        res = []
        for index in self.table:
            for k,v in index:
                res.append((k,v))
        return res
        
        
buku = hashTable(7)
print(f"{'*' * 5} tabel buku {'*' * 5}")
buku.set("nama","filosofi teras")
buku.set("aman","dump")
buku.set("penulis","marcus aurelius")
buku.displayTable()
print(buku.items())

print(f"{'*' * 5} tabel mahasiswa {'*' * 5}")
mahasiswa = hashTable(3)
mahasiswa.displayTable()