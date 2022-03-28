from scipy import *
from matplotlib.pyplot import *
import numpy as np

def f(x):
    return 2*x + 1
z = []
for x in range(10):
    if f(x) > pi:
        z.append(x)
    else:
        z.append(-1)
print(z)
    

