#Everything is regarded as an object
class Person:
    #properties/variables/attributes/Characteristics
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #Behavior/Method/Function
    def study(self):
        print("Student is studying",self.name,self.age,self.gender)
        #Creating an object
student1 = Person("John",23,"Male")
print(student1.study())
student2 = Person("Liam",22,"Male")
print(student2.study())
student3 = Person("Beatrice",22,"female")
print(student3.study())
print(student1.study(), student2.study(), student3.study())
