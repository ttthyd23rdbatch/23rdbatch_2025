x = int(input("Enter the number: "))
if x >0:
    print("Entered number is positive!!")
elif x < 0:
    print("Entered number is negative!!")
else:
    print("Number is Zero!!")


x = int(input("Enter the number: "))
if x % 2 ==0:
    print("Entered number is EVEN")
else :
    print("Entered number is ODD")


a = int(input("Enter your age: "))
if a >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible")


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
else:
    print("Both the numbers are equal")


num = int(input("Enter a year: "))
if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
    print("This is a leap year")
else:
    print("This is not a leap year")


temp = int(input("Enter your current temperature: "))
if temp >= 30:
    print("It's HOT today")
elif 20 < temp > 30:
    print("It's a pleasant weather")
elif temp <= 20:
    print("It's COLD today")


num = int(input("Enter the number"))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both numbers")
elif num % 3 == 0 and num % 5 !=0:
    print("The number is divisible by 3 only")
elif num % 3 != 0 and num % 5 == 0:
    print("The number is only divisible by 5 only")
else:
    print("The number is neither divisible by 3 nor divisible by 5")


p = str(input("Enter the password: "))
if  p == 'admin123':
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
 