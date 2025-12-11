print("hello world")
# Given a string "hello world", convert it to uppercase.
print("hello world".upper())
# conversion of data types
x = 1
y = 2.6
z = 9j
a = float(x)
b = int(y)
c = bool(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
# casting
a = int(2.99)
b = float(600)
print(a)
print(b)

a = "Akshit"
print(a[3])

b = "AKSHIT"
print(len(b))

x = "I am learning python"
if "am" in x:
    print("yes")

b = "today is tuesday"
print(b[2:9])

b = "today is tuesday"
print(b[-9:-2])

x = "I am learning python     "
print(x.strip())

x = "I am learning python"
print(x.replace('learning', 'studying'))

a = 85
x = f'My weight is {a} kg'
print(x)

a = 85
x = f'My weight is {a:.2f} kg'
print(x)

a = f'the area of my land is {50*80} metresq'
print(a)

a = 45
b = 56
if b>a:
    print('b is greater than a')
else:
    print('b is not greater than a')

a = 558
b = 45
print(a / b)

a = 558
b = 45
print(a // b)

