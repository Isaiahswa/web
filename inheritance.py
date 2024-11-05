class Animal:
    def move(self):
        print("Animal is Walking")

    #child class
class Dog(Animal):
    def bark(self):
        print("Dog is Backing")
a= Animal()

d= Dog()
d.move()
d.bark()
