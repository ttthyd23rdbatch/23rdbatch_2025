a = [1,2,3,4,5,6,7]
print(a)
print(type(a))

x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(x[-4:-1])

y = [1,2,3,4,55,6,7,8,9,10,11]
(print(y[4:9]))

a = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
x.remove("kiwi")
print(x)

a = [12,34,65,87,34,22,87]
a.pop(1)
print(a)

a = [12,34,65,87,34,22,87]
a.pop()
print(a)

a = [45,58,2,558,568,55,78,91,35,84,67,25,94,58]
a.sort()
print(a)

a = [12,34,65,87,34,22,87]
b = a.copy()
print (b)

a = [12,34,65,87,34,22,87]
b = list(a)
print(b)

a = [12,34,65,87,34,22,87]
b = a[:]
print(b)

a = ["a", "b", "c"]
b = [1, 2, 3]
c = a+b
print(c)

a = (12,34,65,87,34,22,87)
print(type(a))
b = list(a)
print(b)
print(type(b))

a = (78,95,76,93,91)
b, c, d, e, f = a
print(b)
print(c)
print(d)
print(e)
print(f)

a = {78,95,76,93,91}
print(type(a))

a = {1, 2, 3, 4}
print (a)
a.add(5)
print (a)

a = {10,20,30}
b = {40,50}
a.update(b)
print(a)

x = {"a","b","c","d"}
x.update(["e","f","g"])
print(x)

a = {100,50,20,920,45,450}        #If the item to remove does not exist, remove() will raise an error whereas discard() will not raise any such error.
a.remove(100)
print(a)

a = {1,5,2,4,6,3}
a.discard(8)
print(a)

a = {"apple","banana","mango","orange"}
print(a)
b = a.pop()
print(b)
print(a)

a = {"apple","banana","mango","orange"}
print(a)
a.clear()
print(a)

num = {100,200,300,400,500}
num.discard(200)
print(num)

data = {10,20,30,40,50,100,5,45,54,8}
small = min(data)
data.remove(small)
print(data)

a= {'a','b','c','d','e'}
if 'z' in a :
    a.remove('z')
else :
    print("Element not found")

item  = {1,2,3,4,5,6}
for num in list(item):
    if num % 2 ==0:
        item.remove(num)
print(item)

a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print(c)

a = {1, 2, 3}
b = {3, 4, 5}
c = a | b
print(c)

a = {1, 2, 3}
b = [3, 4, 5, 6]
c = a.union(b)
print(c)

a = {5,10,15,20,25,30}
b = {10,20,30,40}
c = a|b
print(c)

a = {5,10,15,20,25,30}
b = {'x','y','z'}
c = a|b
print(c)

a = {1,2,3,4,5,6}
b = {7,8,9,11,10}
a.update(b)
print(a)

a = {1,2,3,4,5}
b = {6,7,8,1,5,4,9,10}
c = a.intersection(b)
print(c)

a = {5,4,6,8,2,3}
b = [9,6,4,8,2,5,7]
c = a.intersection(b)
print(c)

a = {
    "name" : "Akshit",
    "age" : 22,
    "city" : "Dehradun",
    "Branch" : "CSE"
}
print(a)

a = {
    "name" : "Akshit",
    "age" : 22,
    "City" : "dehardun",
    "Branch" : "CSE"
}
print(a)
a["current city"] = "Miyapur"
print(a)

marks = {
    "maths" : 91,
    "physics" : 89,
    "chemistry" : 70,
    "english" : 55
}
print(marks)
marks.update({"english" : 85})
print(marks)

data = {
    "name" : "Akshit",
    "age" : 22,
    "city" : "dehradun",
    "course" : "B.Tech",
    "branch" : "CSE"
}
print(data)
data.pop("branch")
print(data)

prices = {
    "mango" : 50,
    "apple" : 40,
    "guava" : 60,
    "grapes" : 40
}
print(prices)
if "orange" in prices:
    print("Found")
else :
    print("Not Found")

car = {
    "brand" : "toyota",
    "year" : 2022,
    "model" : "fortuner"
}
print(car)
new_car = car.keys()
print(new_car)

data = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5
}
print(data)
new_data = data.values()
print(new_data)

stu = {
    "name" : "Akshit",
    "age" : 22,
    "course" : "B.Tech",
    "branch" : "CSE"
}
print(stu)
new_stu = stu.get("course")
print(new_stu)

num = {
    "one" : 1,
    "two" : 2,
    "three" : 3
}
print(len(num))

