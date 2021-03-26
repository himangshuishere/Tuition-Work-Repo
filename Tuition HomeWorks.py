# HomeWork Solution
"""
Q.1.Find the largest number from three user given numbers.
"""
# Solution:
a, b, c = eval(input("Enter three numbers: "))

if a > b and a > c:
    print(f"{a} is the largest among all numbers!")

elif b > a and b > c:
    print(f"{b} is the largest among all numbers!")

else:
    print(f"{c} is the largest among all numbers!")


"""
Q.2.Test whether the user given number is positive/negative or equal to zero.
"""

# Solution
userNum = float(input("Enter your number: "))

if userNum < 0:
    print(f"{userNum} is negative number")

elif userNum > 0:
    print(f"{userNum} is positive number")

else:
    print(f"{userNum} is equal to 0")

"""
Q.3.Test whether a user given year is leap year or not
"""
# Solution
year = int(input("Enter year: "))
if year % 4 == 0:
    if year%100 == 0:
        if year %400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

"""
Q.4. find out roots of quadratic equation whose polynomials are given by user
"""
# Solution
a, b, c = eval(input("Enter three coefficients of quad equation: "))
equation = f"{a}x² + {b}x + {c}"
print()
print(f"User-given equation is:\n{equation}")

discriminant = pow(b,2) - (4*a*c)

root1 = (-b - pow(discriminant,0.5))/(2*a)
root2 = (-b + pow(discriminant,0.5))/(2*a)

if root1 == -(root2):
    print(f"The roots of '{equation}' is: ±{root2}")
else:
    print(f"The roots of '{equation}' are: {root1} and {root2}")


"""
Q.5.Test whether a triangle is equilateral or scalene or isosceles.
"""

# Solution
print("How you want to determine the name of triangle?\n1.By using side-length\n2.By using interior angles")
choiceInput = int(input("Enter your choice: "))
a = False
name = ""

if choiceInput == 1:
    a, b, c = eval(input("Enter three sides length(in cm): "))
    print(f"The three sides of triangle are:\n{a} cm, {b} cm, {c} cm, and ...")

    if a == b == c:
        name = "Equilateral"
    
    if a == b != c or a != b == c or a == c != b:
        name = "Isosceles"
    
    if a != b != c:
        name = "Scalene"
    
    print(f"The name of the Triangle is {name}")

if choiceInput == 2:
    a, b, c = eval(input("Enter the value of three interior angles(in deg.): "))
    print(f"The three interior angles of triangle are:\n{a}° , {b}°, {c}°, and ...")

    if a == b == c:
        name = "Equilateral"
    
    if a == b != c or a != b == c or a == c != b:
        name = "Isosceles"
    
    if a != b != c:
        name = "Scalene"
    
    print(f"The name of the Triangle is {name}")


"""
Q.6.Test whether a given character is uppercase or lowercase letter using its ASCII value
"""
userChar = input("Enter a letter: ")

if ord(userChar) >= 65 and ord(userChar) <= 90:
    print(f"{userChar} is an UpperCase Character according to ASCII test.")

if ord(userChar) >= 97 and ord(userChar)<=122:
    print(f"{userChar} is a LowerCase Character according to ASCII test.")


"""
Q.7.Test whether a given character is vowel or consonant.
"""
userChar = input("Enter a character: ")

if userChar.casefold() in "aeiou":
    print(f"{userChar} is a vowel")

else:
    print(f"{userChar} is a consonant")

"""
Q.8.Test whether a number is even or odd if it is positive, otherwise test the number is negative or equal to zero or not
"""

userNumber = eval(input("Enter a number: "))

if userNumber > 0:
    if userNumber%2 == 0:
        print(f"{userNumber} is a positive even number.")
    else:
        print(f"{userNumber} is a positive odd number.")

elif userNumber < 0:
    print(f"{userNumber} is a negative number.")

else:
    print(f"{userNumber} is equal to 0")

"""
Q.9.Findout largest and smallest number out of three user given numbers
"""

a, b, c = eval(input("Enter three numbers: "))
smallest = 0
largest = 0
if a>b and a>c:
    largest = a
    if b>c:
        smallest = c
    else:
        smallest = b

elif b>a and b>c:
    largest = b
    if c>a:
        smallest = a
    else:
        smallest = c

else:
    largest = c

print("The largest number is: ", largest)
print("The smallest number is: ", smallest)


