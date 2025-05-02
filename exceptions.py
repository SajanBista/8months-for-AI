#Error and exceptions 
#type error
"""a = 5 + '10'
print(a)
"""

#import error
"""import ran
"""
#file not found error
"""f = open(somefile.text)"""

#index error
"""a = [1,2,3,4]
a.remove(5)
print(a)
"""
#key error
"""a = {'name':'max'}
a.['age']"""

"""x = -5
if x <0:
    raise Exception('x should be positive')

#assertion error 
assert (x >=0), 'x is not positive'
"""

"""
#Exception
try:
    a = 5/1
    b = a + 1

except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print(" everything is fine ")
finally:
    print('cleaning up......')
"""
print("________________________________________________________________________")

class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self,message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x >100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooLowError('value is too small')
    
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)






