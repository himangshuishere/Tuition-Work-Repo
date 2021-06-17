# find the number of digits in user-given number, sum of digits, each digit print and reverse numbner print of a number given by user.
n = int(input("Enter number: "))
d = s = t =count = sum = 0
s=n
while n!=0:
    d = n%10
    print(d)
    count+=1
    t = (t*10)+d
    sum +=d
    n//=10
print("Total digits: ", count)
print("Sum of digits: ", sum)
print("Reverse number: ", t)
if s == t:
    print("This is a Palindrome number.")
else:
    print("This is not a Palindrome number.")
