class Animal:
    umur = 12
    def owner():
        print("juana")
    def sound(self):
        print("This is the original Sound of animal")
        
class Dog(Animal):
    def sound(self):
        super().owner
        umur = 0
        print(umur) 
        umur = super().umur
        print(umur) 
        print("guk guk guk")
        
print("dog")
emon = Dog()
emon.sound()

print("hewan")
hewan = Animal()
hewan.sound()
