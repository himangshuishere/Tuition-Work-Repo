#rangeUser = int(input("Enter range: "))
#a, b, c = 0, 1, 0
#print(a, b , end=" ")
#i = 3
#while i<=rangeUser:
 #   c = a + b
  #  print(c, end= " ")
   # a,b = b, c
    #i +=1


# Find the factorialof  a number
userInput = int(input("Enter number: "))
fact = 1
for i in range(1, userInput+1):
    fact*=i
print(fact, "is the factorial value of", userInput)
