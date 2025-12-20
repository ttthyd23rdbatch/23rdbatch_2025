# 1️⃣ Print numbers from 1 to 10 using a for loop.
#
# 2️⃣ Print numbers from 10 to 1 using a while loop.
#
# 3️⃣ Print all even numbers from 1 to 20.
#
# 4️⃣ Print all odd numbers from 1 to 20.
#
# 5️⃣ Print the word “Python” 5 times.

# for i in range(1,11):
#     print(i)

# i=10
# while i>0:
#     print(i)
#     i=i-1

# for i in range(1,21):
#     if i%2==0:
#         print(i)

# for i in range(1,21):
#     if i%2==1:
#         print(i)

# word="Python "
# print(word * 5)
# for i in range(5):
#     print("Python")

# 6️⃣ Given a list, print each element.

# a=[1,2,3,4,5]
# for i in a:
#     print(i)

# 7. Print numbers from 1 to 10, but skip 5.

# for i in range(11):
#     if i==5:
#         continue
#     print(i)

# 8.Print numbers from 1 to 10, but stop when number is 7.

# for i in range(11):
#     if i==7:
#         break
#     print(i)

#9.Print only numbers greater than 50 from a list.
#
# a=[10,60,45,80,30]
# for i in a:
#     if i>50:
#         print(i)

# 10.Find the sum of numbers from 1 to 10.
# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)

#11.Print the multiplication table of 5.

# i=1
# while i<=10:
#     x=i*5
#     print("5 *",i,"=",x)
#     i = i + 1

#12.Print this pattern:

# *
# **
# ***

# for i in range(1,4):
#     print("* " * i)


#13. Print this pattern:
#
# 1
# 12
# 123

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#14.Print a 3 × 3 star pattern.
# for i in range(3):
#     for j in range(3):
#         print("* ",end="")
#     print()
#

#15.Find the largest number in a list using a loop.

# 16.Count how many even numbers are in a list.
#
# 2️⃣1️⃣ Check whether a number is prime or not.
#
# 2️⃣2️⃣ Find the factorial of a number using a loop.

# a=[1,2,3,4,5,6]
# largest=a[0]
# for i in a:
#     if i>largest:
#         largest=i
# print(largest)

# a=[1,2,3,4,5,6,7,8,9]
# count=0
# for i in a:
#     if i%2==0:
#         count+=1
# print(count)

# n=int(input())
# l=[]
# count=1
# for i in range(1,n+1):
#     l.append(i)
# for j in l:
#     count=count*l
# print(count)