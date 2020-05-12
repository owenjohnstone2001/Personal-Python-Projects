from scipy import random
import numpy as np
import matplotlib.pyplot as plt
import math

a = 0
b = 1
N = 31623
areas = []

def func(x):
    y = math.exp(-1 * (x ** 2))
    return y

for i in range(N):
    xrand = random.uniform(a,b,N)
    integral = 0

    for i in range(N):
        integral += func(xrand[i])
    areas.append((b - a) * integral / N)
    
plt.title('Distribution of Areas Calculated')
plt.hist(areas, bins = 100, ec = 'black')
plt.xlabel("Areas")
plt.show(block = True)