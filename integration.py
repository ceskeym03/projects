import math 
import numpy
import matplotlib as plt


## INTEGRATION CALCULATOR

def f(x):
    return lambda x: f


def integration_calculator(f):
    a = float(input('What is the lower bound'))
    b = float(input('What is the upper bound'))

    n=int(input('How many different inputs'))
    delta = (b-a)/n
    return print(sum(f(a+i*delta)*delta for i in range(1,n+1)), a, b, n)

def integration_calculator_trig(f):
    a = float(input('What is the lower bound'))
    b = float(input('What is the upper bound'))

    n=int(input('How many different inputs'))
    l=math.radians(b)
    delta = (l-a)/n
    return print(sum(f(l+i*delta)*delta for i in range(1,n+1)), a, l, n)