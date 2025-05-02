#lambda arguments:expression

#here it has single argument
add10 = lambda x:x +10
print("this is the output of lambda function \n")
print(add10(5))

def add_func(x):
    return x +10

print("this is the output of normal function\n")
print(add_func(5))


print("________________________________________________________________________")

#taking multiple argument in lambda 
mult = lambda x,y: x+y

print(mult(10,4))

def mul_func(x,y):
    return x*y
print(mul_func(10,4))

print("________________________________________________________________________")

point2D = [(1,2),(15,1),(5,-1),(10,4)]
print("this is the sorted list of done by lambda")
sorted_list = sorted(point2D, key = lambda x: x[0] + x[1])
print(sorted_list);

"""def sort_by_y(x):
    return x[1]
x =[[(1,2),(15,1),(5,-1),(10,4)]]

print(sort_by_y(x))"""
print("________________________________________________________________________")
#map function
# #map(func, seq)

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

print("________________________________________________________________________")
#filer function
#filter(func,seq)

a = [1,2,3,4,5]
b = filter(lambda x: x%2==0, a)
print(list(b))

c = [x for x in a if x%2 ==0]
print(c)


print("________________________________________________________________________")

#reduce(func, seq)


from functools import reduce
a = [1,24,5,67,9]

product_a = reduce(lambda x,y: x*y,a)

print(product_a)