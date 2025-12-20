'''Dictionary are used to store data values in key value pair
    simply we say each value stored in each key
    dictiory written in curly brackets {key:value}
    dictionary are order and changeable and do not alow duplicates
    keys should be mutable 
    values sjhould be immutable
    in dictionary keys acts as a indexing and no slicing
    keys are unique'''

'''Accessing items by refering the dictionary keys in the square brackrts'''

a={"name":"venky","Age":23,"City":"Hyd"}
# print(a["name"])

#Dictionasry methods

#GET() is used to acces items of a dictionary by referring get method

# print(a.get("Age"))

#KEYS(): keys() method id used to return list of all keys
#values(): values ( method is used to return all list of vslues)

# print(a.keys())

# print(a.values())

#items(): items(method is used return all values and keys in dictiinary key pair items)

# print(a.items())

# update() method is used to to add new key value pair or updating existing ones in dictionary

# a.update({"course":"Python"})
# print(a)

# a.update({"name":"anil"})
# print(a)

#removing items

#pop(): pop ( ) method is ised to remove a specific key value pair from a dict using key
# 
# a.pop("name")
# print(a)
# print(a)

# a.update({"Name":"Durga"})
# print(a)

#POPITEM(): popitem method id used to remove last insertd item
# a.popitem()
# print(a)

# del(): del method  is used to delete a item in the dic or dele entire dic

# del a

#clear: method is used to remove all the elemnts from the dictionary
# a.clear()
# print(a)

#COPYDICTIONARIES

#copy(): is used to craete a copy a  dictionary with same data

# b=a.copy()

#dict() it is another way of copying
# b=dict(a)
# print(b)

#you can also accesing the items in dictionary by using loop through

for i in a:   #getting keys only
    print(i)

for j in a:    #return values
    print(a[j])


for i in a.values():
    print(i)
for j in a.keys():
    print(j)
for i,j in a.items():
    print(i,j)  