GREEN = '\u001b[32m'
CYAN = '\u001b[36m'
RESET = '\u001b[0m'
RED = '\u001b[31m'
MAGENTA = '\u001b[35m'

import colorama
colorama.init()
print(f"{GREEN}")

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

print("---------------------------------------------------------------------------")
print(f"{CYAN}")
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
print(f"Perimeter of circle is: {circleAreaPerimeter[0]:.2f}cm")
print(f"Area of Circle is: {circleAreaPerimeter[1]}cm²")
    
print()
print("-----------------------------------------------------------")
print(f"{RED}")

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
    
schoolName = input("Enter school name: ")
studentName = input("Enter student name: ")
subjectMarks = eval(input("Enter subjects marks in list format: "))
totalSubjectsNumber = int(input("Enter total number of subjects: "))
totalMarksforEachSubject = int(input("Enter total marks alloted for each subject: "))
grade(schoolName,studentName, subjectMarks, totalSubjectsNumber, totalMarksforEachSubject)

print()
print("----------------------------------------------")
print(f"{GREEN}")
def factorial(number: int = ...)-> int:
    fact = 1
    for i in range(1, number+1):
        fact *= i
    
    return fact


UserNumber = int(input("Enter number: "))
print(factorial(UserNumber))
