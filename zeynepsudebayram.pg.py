import numpy as np

def factorial(n):
    result = 1
    if n == 0:
        result = 1
    else:
        for i in np.arange(1,n+1):
            result = result * i
    resturn result
    
if factorial(3) == 6:
    print("No errors")
    


