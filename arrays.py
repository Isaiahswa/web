courses=["MIT", "Cybesrsecurity", "Datascience"]
print(courses)

#Accessing an element in array
print(courses[1])

#looping through an element
for x in courses:
    print("our courses are", x)
#Adding a new element into an array
courses.append("Web Development")
print(courses)

#Deleting an element in array
courses.remove("MIT")
print(courses)