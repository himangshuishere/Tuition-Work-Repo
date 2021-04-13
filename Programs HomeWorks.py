L = [17,19, 21, 27, 31]
# Right shift of first term to last term
for i in range(len(L)):
    if i == 1:
        a = L.pop(0)
        L.append(a)
    else:
        pass

print("List after shifting the first element to the last: ", L)

L = [17,19, 21, 27, 31]
#Left shift of last term to first
for i in range(len(L)):
    if L[i] == L[-1]:
        a = L.pop(-1)
        L.insert(0, a)
    else:
        pass

print("List after shifting the last element to the first: ", L)


# !-------------------------------------------------------!
# !                    Functions                          !
# !-------------------------------------------------------!

# Perimeter and area of circle

def circle(radius: float = ..., pieValue: float = 3.14)-> list:
    """
    This function returns the `list` containing `perimeter` and `area` respectively.

    Args:
    `radius`: This argument can be `float` or `int` data type

    `pieValue`: This argument should always be in `float` data type
    """
    
    perimeter = 2*radius*pieValue
    area = pieValue*(radius**2)
    
    return [perimeter, area]


radiusCircle = float(input("Enter radius in cm: "))
pieCircle = float(input("Enter pie's value: "))
circleAreaPerimeter = circle(radiusCircle, pieCircle)
print("Perimeter of circle is: ", circleAreaPerimeter[0]," cm")
print("Area of Circle is: ", circleAreaPerimeter[1], " cm²")
    

def grade(schoolName: str=..., studentName : str = ..., SubjectMarks: list = [], totalSubjects: int = 6, totalMarksForEachSubject: int = 80)-> None:
    print("+-------------------Report Card----------------------+")
    print("|",schoolName.center(50-1)," |")
    print("+----------------------------------------------------+")
    print("Candidate: ", studentName)
    grading = ""
    totalOfSixSubjects = sum(SubjectMarks)
    percentage = (totalOfSixSubjects/(totalSubjects*totalMarksForEachSubject))*100
    if percentage >= 91:
        grading = "A+"
    elif percentage >= 81:
        grading = "A"
    elif percentage >= 71:
        grading = "B+"
    elif percentage >= 61:
        grading = "B"
    elif percentage >= 51:
        grading = "C"
    elif percentage >= 41:
        grading = "D"
    elif percentage >= 31:
        grading = "E"
    else:
        grading = "Fail"
    print()
    print(f"Percentage: {percentage:.2f}%")
    print()
    print("Grade: ", grading)
    if grading == "Fail":
        print()
        print("Student has failed and demoted to current class")
    

# grade()


def factorial(number: int = ...)-> int:
    fact = 1
    for i in range(1, number+1):
        fact *= i
    
    return fact


UserNumber = int(input("Enter number: "))
print(factorial(UserNumber))