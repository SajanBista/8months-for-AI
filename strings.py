#String : Ordered, immutable, text representation
"""
my_string = Hello  I'm \
    starting AI/ML
print(my_string)


#accessing the string 
my_string = "Hello programmer "
char =my_string[0]
print(char)
print(my_string[-1])


substring = my_string[1:5]
print(substring)

#sting concatination 

name = "sajan"

group = "programmer"

invit = "hello"

total_sentence = invit + " "+ group + " "+ name
print(total_sentence)

for i in group:
    print(i)

if 'p' in group:
    print("yes ")
else:
    print("no letter p")

mystring = "i am checking"
print(mystring.upper())

print(mystring.count('c'))

print(mystring.replace('checking','trying all the thing for printing and learning ai and machine learning'))
mylist1 = mystring.split(" ")
print(mylist1)
mylist = list(mystring)
print(mylist)


from timeit import default_timer as timer



my_list = ['a']*12000
#print(my_list)

start = timer()
#good practice
my_string = ''.join(my_list)
#print(my_string)
stop = timer()
print(stop-start)

start = timer()
#bad practice 
my_string = ''
for i in my_list:
    my_string +=i
#print(my_string)
stop = timer()
print(stop-start)
"""


#formating methods
# %, .format(), f-strings

#old
name = input(str("enter your name"))
age = 20

my_string = "hello %s welcome to the programmer zone" % name
print(my_string)

#new method
my_string = "the variable is {} and age is {}".format(name, name)
print(my_string)

aim ="ai developer"

#now new and the best way of doing it 

my_string = f"hi mr. {name} you are {age} years old and aming to be {aim}"
print(my_string)
