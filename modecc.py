import matplotlib.pyplot as plt 
import numpy as np

a = -5
b = 5
prime = 97

def add_inverse(value):
    global prime
    answer = -1 * (value % prime) + prime
    return answer

def mult_inverse(value):
    global prime
    #answer = (value%prime) ** (prime-2) % prime
    answer = pow(value, -1, prime)
    return answer #, answer * value %prime
def sqrerootfinder(answer):
    global prime
    modanswer = answer % prime
    for i in range(prime):
        if i **2 % prime == modanswer:
            return i

def f(x):
    global a; global b
    return sqrerootfinder(x** 3 + a * x + b)

def point_addition(Px,Py,Qx,Qy):
    global prime; global a; global b
    if Px == Qx:
        num = 3* Px**2 + a % prime
        den = 2 * f(Px) % prime
    else:
       
        num = (Py - Qy) % prime
        den = (Px - Qx) % prime
    gradient = (num * mult_inverse(den)) % prime

    x = (gradient ** 2 - Px - Qx) % prime
    y = (gradient * (Px - x)- Py) % prime
    return x,y

def point_multiplication(Px,Q,n):
    Py = f(Px)
    Qx,Qy = Q
    if Qx < 0:
        Qx, Qy= point_addition(Px,Py,Px, Py)
    for i in range(n):
        print(Qx,Qy)


        Qx,Qy = point_addition(Px,Py,Qx,Qy)
    print(f"public key: ({Qx},{Qy})")

#A
Generator = 7
initial = (-1,-1)
privatekey1 = 5
point_multiplication(Generator,initial,privatekey1)

#B
publickey1 = (92,14)
privatekey2 = 14
point_multiplication(Generator,publickey1,privatekey2)

#B
initial = (-1,-1)
point_multiplication(Generator,initial,privatekey2)

#A
publickey2 = (61,63)
point_multiplication(Generator,publickey2,privatekey1)