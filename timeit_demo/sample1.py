import timeit


testcode = ''' 
import random
def test(): 
    return random.randint(10, 100)
'''


print(timeit.repeat(testcode))

