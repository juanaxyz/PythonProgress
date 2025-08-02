class Mobil:
    def __init__(self, merk: str, kecepatan: int):
        self.merk = merk
        self.kecepatan = kecepatan

    def jalan(self):
        print(f"{self.merk} sedang berjalan dengan kecepatan {self.kecepatan} km/jam")


miniCooper = Mobil("mini cooper", 100)

miniCooper.jalan()
