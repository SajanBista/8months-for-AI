#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product,permutations, combinations,combinations_with_replacement, accumulate, groupby
import operator
a = [1,2,3,10,5]
b = [3,4]


print("the result of product is \n")
prod = product(a,b, repeat = 2)
print(list(prod))



"""  #try
per = permutations(a,b, repeat = 2)
print(list(permutations))


comb = combinations(a,b,repeat = 2)
print(list(combinations))

acc = accumulate(a,b)
print(acc)

group_by = groupby(a,b)
print(group_by)
"""
print("the result of permutaion  is \n")
per = permutations(a)
print(list(per))


comb_without_replacement = combinations(a,2)
print("the result of combination without replacement is \n")# will also make combination with itself
print(list(comb_without_replacement))

comb = combinations_with_replacement(a,2)#length is mendatory as this will make possible combination with 2 elements on each matrix
print("the result of combination is \n")
print(list(comb))

print("the result of accmulation is \n")
acc = accumulate(a)
print(list(acc))# default it is sum


print("the result of accmulate function for multiplication is \n")
acc_mul = accumulate(a, func = operator.mul)
print(list(acc_mul))# this is giving multiplication



print("the result of accmulate function for max is \n")
acc_mul1 = accumulate(a, func =max)
print(list(acc_mul1))


def smaller_than_3(x):
    return x<3

group_obj = groupby(a, key= smaller_than_3)
for key, value in group_obj:
    print(key, list(value))


group_obj1 = groupby(a, key= lambda x: x<3)# using lambda function so it will be easier  and code will be shorter
for key, value in group_obj1:
    print(key, list(value))


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 22},
    {"name": "Eve", "age": 35}
]

people_sorted = sorted(people, key=lambda x: x['age'])

groupby_real_example = groupby(people_sorted, key = lambda x: x['age'])
for key, value in groupby_real_example:
    print(key, list(value))


from itertools import cycle, count, repeat

a = [1,2,3]

"""for i in cycle(a):
    print(i)"""
count =0
for i in repeat(a,100):
    print(i)
    count +=1
print(count)