a = input()
print(int(a) + int(a))

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print(f"The sum of {num1} and {num2} is {int(num1) + int(num2)} ")

x = input("Enter your age")
print(f"After 5 years you will be {int(x) + int(5)} years old")

q = input("Enter the length: ")
p = input("Enter the breadth: ")
print(f"The area of the rectangle is {int(q) * int(p)}")

x = str(input("Enter the string whose length you want to know: "))
print(f"the length is {len(str(x))}")

num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Entered number is even!")
else :
    print("Entered number id odd")

fname = str(input("Enter your first name: "))
lname = str(input("Enter your last name: "))
print(f"your full name is {fname} {lname}.....")

m = int(input("Enter the marks of maths: "))
s = int(input("Enter the marks of science: "))
p = int(input("Enter the marks of python: "))
av = (m + s + p)/3
print(f"The average marks are: {av}")