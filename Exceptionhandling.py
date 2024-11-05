#any error you encounter
try:
  number=1
  print(number)
except:
    print("An error occurred")
try:
 num1=39
 num2=8
 print(num1/num2)
except:
    print("A ZeroDivisionError occurred")

finally:
    print("success")



