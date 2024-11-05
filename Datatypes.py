#datatypes
number = 67 #integer
second=45.98 #float
greetings = "Hello There!" #string
isPythonInteresting =True #Bolean
print(number,second,greetings, isPythonInteresting)

#Data Structures- Multiple values stored in a single variable
cars= ["Toyota","Nissan","Vw"] #Lists-Ordered and also changeable
fruits=("banana", "apple", "mango") #This is a tuple but unchangeable
countries = {"Kenya", "Tunisia", "Algeria"} #Set - Unordered and also unchangeable
student = {
    "firstname" : "jane",
    "age" : 25,
    "course": "Web Development",
    "gender" : "Female"
} #Dictionary - Key-Value Pair
print("isaiah drives",cars, "he loves",fruits, "he has visited",countries, "school details are",student["gender"])
print(student["gender"])

#Determining a Datatype
print(type(countries))
print(type(student))

#Typecasting - converting from one data type to another
print(float(number))
print(int(second))




