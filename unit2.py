#intermediate python course in 6 hours


#This unit is all about the self practice and here i did all thing of list, tuples, set and dictionary
#list
"""mylist = ["banana", "cherry", "appple"]
item = mylist[0]

for i in mylist:
    print(i)

print(item)
print(mylist)

if "banana" in mylist:
    print("yes")
else:
    print("banana is yet to append which means it isn't in the list ")


#check length
print(len(mylist))
mylist.append("avocardo")
print(mylist)
mylist.append(3,"blueberry")

mylist.pop()
print(mylist)

mylist.remove("cherry")

item = mylist.sort()
item =mylist.reverse()"""



"""mylist = [0] * 5

mylist1 = [1,2,3,4,5]
newlist = mylist + mylist1
print(newlist)

a = mylist[1:5:2]
print(a)"""

"""list_original = ["apple","banana", "cherry"]
list_Copy = list_original#this is the wrong method if i change the original list all the things will be changed
list_copy1 = list(list_original)#this will also make the different copy means if i changes in the copied code original will stay same that as before
list_copy = list_original[:]# way of copying list that copied list and the actual list are different here
list_copy.append("ram")
print(list_Copy)
print(list_copy1)
print(list_copy)
print(list_original)"""

"""
I=2
my_list = [i for i in range (10)]
my_list1 = [i*I for i in range(10)]
print(my_list1)
print(my_list)
my_list.append(my_list1)
print(my_list)
"""

#Tuples: orderd, immutable, allows duplicate elements

"""mytuple = tuple(["Mac", 1, "1.334"])
print(mytuple)

item = mytuple[0]
print(item)
print(mytuple[-2])

#mytuple[0] = "Apple"#doesn't allow to enter so error "'tuple' object does not support item assignment"
print(mytuple)

if 1 in mytuple:
    print("yes")
else:
    print("no max")
"""

#create tuple with some letters

"""my_tuple = ('a','p','p','l','e')

print(my_tuple.index('p'))
#print(my_tuple.index(x))#NameError: name 'x' is not defined
print(len(my_tuple))

my_list = list(my_tuple)

my_list.append("appended")
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)"""
"""slicing 
a = (1,2,3,4,5,6,7,8)
b = a[2:8:2]

c = a[:: -1]
print(c)
print(b)
"""
"""
my_tuple = "sajan", 20 , "Kathmandu"
name, age, address = my_tuple

i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)

print(name)
print(age)
print(address)
"""

"""according to my understanding sys module provide access to system specific parameter and the function.It allows you to interact with the python runtime ennvironment
import sys
my_list = [1,2,3, "hello", True]
my_tuple = (1,2,3, "hello", True)
print(sys.stdout.write("i am learning python for my ml and ai project"))
print(sys.stderr.write("You might get multiple error doing coding"))
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")


import timeit
print(timeit.timeit(stmt = "[0, 1, 2, 3, 4, 5]", number = 100000))
print(timeit.timeit(stmt = "(0, 1, 2, 3, 4, 5)", number = 100000))
working with tuple is more faster as in the list i got it from the above code"""

#Dictionary : key-value pairs, unordered, mutable 
"""
my_dict =dict(name ="sajan", age =20, city = "kathmandu")
print(my_dict)

print(my_dict["name"])

my_dict["email"]="sajan1030@gmail.com"
print(my_dict)

del my_dict["age"]
print(my_dict)

my_dict.pop("name")
print(my_dict)
my_dict.popitem()
print(my_dict)

if "name" in my_dict:
    print(f"your name is  {my_dict['name']}")
else:
    print("no name found")


try:
    print(f"your age is {my_dict["age"]}")
except:
    print("no age found error")

for key in my_dict:
    print(key)

for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)


for key,value in my_dict.items():
    print(key,value)

my_dict_copy = my_dict#if you modify the copy also you original will also be modified 

my_dict_copy1 = my_dict.copy()
my_dict_copy2 = dict(my_dict)
my_dict_copy["appending"] = "appended"
my_dict_copy1["appending"] = "appended"
my_dict_copy2["appending"] = "appended"

print(my_dict)#orginal 
print(my_dict_copy)
print(my_dict_copy1)
print(my_dict_copy2)

"""

#merging 

"""my_dict1 ={"college":"NSC", "Name":"sajan", "Age":20}
my_dict2 = {"faculty":"bca", "semester":5}
my_dict1.update(my_dict2)
print(my_dict1)
mydict_merged = my_dict1 | my_dict2

print(mydict_merged)


my_tuple =(8,7)
mydict ={my_tuple:15}
print(mydict)
"""



#set is unordered, mutable and no duplicate values

#myset = set("Hello")
#print(myset)

"""myset =set()
#print(type(myset))
myset.add(1)
myset.add("ram")
myset.add(2)
myset.add(2)#will not print two 2 because it doesn't allows the duplicate values 
print(myset)

myset.remove("ram")# this will not return the error nor remove the way of removing is discard function or clear()
myset.discard("ram")

print(myset)
print(myset.pop())
#myset.clear()
print(myset)


myset =set()
for i in range (10):
    myset.add(i)
print(myset)

if 4 in myset:
    print("yes 4 is in the set")
else:
    print("no 4 is seen  in the set ")

#myset.remove(5)#remove specific value 
#myset.clear()#remove whole set value
print(myset)

myset_odds = set()
myset_even = set()
for i in range (10):
    if i%2==0:
        myset_even.add(i)
    else:
        myset_odds.add(i)
print(myset_even)
print(myset_odds)


prime_number = set()

for num in range(2,10):
    #is_prime = True#Assume the number is prime
    for i in range(2, int(num**0.5)+1): ## Check divisors up to the square root of the number
        if num % i ==0:
           # is_prime = False
            break
    else:
        prime_number.add(num)

print(prime_number)

union = myset_odds.union(myset_even)
print(union)
intersection = myset_odds.intersection(myset_even).union(prime_number)
print(intersection)
"""

"""
setA = { 2,4,5,6,20
}
setB ={3,6,7,2}

diff = setB.difference(setA)
print(diff)

print(setB.issuperset(setB))
print(setB>setA)
"""
setA =set()
for num in range (2,20):
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            break
    else:
        setA.add(num)
print(setA)


setB = set()
for i in range (20):
    setB.add(i)
print(setB)

setC=set()
for i in range(20):
    if i%2 ==0:
        setC.add(i)
    
print(setC)

print(setA.issuperset(setB))
print(setA.isdisjoint(setC))
print(setB.difference(setA))

#set copying method

setA_copy = setA.copy()


#frozen set 

a = frozenset([1,2,3,4,5,6,7,8])

a.add(10)
a.remove(2)
a.clear()
print(a)

