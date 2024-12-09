import matplotlib.pyplot as plt 
import numpy as np

prime = 97
a = -5
b = 5

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
def reset():
    with open('personA.txt', 'w') as file:
        file.write("0\n")
    with open('personB.txt', 'w') as file:
        file.write("0\n")
    with open('transfer.txt', 'w') as file:
        for i in range(4):
            file.write("0\n")

    print("Reset")
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
        #print(Qx,Qy)


        Qx,Qy = point_addition(Px,Py,Qx,Qy)
    #print(f"public key: ({Qx},{Qy})")
    return [Qx, Qy]


with open('publicinformation.txt', 'r') as public:

    public_array = [int(line.strip()) for line in public]

    Generator = public_array[0]
    prime = public_array[1]
    a = public_array[2]
    b = public_array[3]
while True:
    whichperson = input("Person A or person B: ")
    if whichperson == "A" or whichperson == "a":
        whichperson = "A"
        break
    elif whichperson == "B" or whichperson == "b":
        whichperson = "B"
        break
    elif whichperson == "reset":
        reset()
    else:
        print("Enter A or B ")

sendrecieve = input("Are you sending (S) or recieving (R): ")
if "R" in sendrecieve or "r" in sendrecieve:
    if whichperson == "A":
        with open('transfer.txt', 'r') as public:
            transfer_array = [int(line.strip()) for line in public]
            publickeyB = (transfer_array[2],transfer_array[3])
        with open('personA.txt', 'r') as file:
            personA_array = [int(line.strip()) for line in file]
            privkeyA = personA_array[0]
        sharedvalue = (point_multiplication(Generator,publickeyB,privkeyA))
        print("shared value:", sharedvalue)
        personA_array.append(sharedvalue[0])
        with open('personA.txt','w') as file:
            for i in personA_array:
                file.write(f"{i}\n")


    else:
        with open('transfer.txt', 'r') as public:
            transfer_array = [int(line.strip()) for line in public]
            publickeyA = (transfer_array[0],transfer_array[1])
        with open('personB.txt', 'r') as file:
            personB_array = [int(line.strip()) for line in file]
            privkeyB = personB_array[0]
        sharedvalue = (point_multiplication(Generator,publickeyA,privkeyB))
        print("shared value:", sharedvalue)
        personB_array.append(sharedvalue[0])
        with open('personB.txt','w') as file:
            for i in personB_array:
                file.write(f"{i}\n")


else:

    privkey = int(input(f"Enter private key for person {whichperson} "))
    initial = (-1,-1)
    with open('transfer.txt', 'r') as public:
        transfer_array = [int(line.strip()) for line in public]

    if whichperson == "A":
        with open('personA.txt', 'w') as file:
                file.write(f"{privkey}\n")
        publickeyA = point_multiplication(Generator,initial,privkey)
        transfer_array[0] = publickeyA[0]
        transfer_array[1] = publickeyA[1]
    else:
        with open('personB.txt', 'w') as file:
            file.write(f"{privkey}\n")
        publickeyB = point_multiplication(Generator,initial,privkey)
        transfer_array[2] = publickeyB[0]
        transfer_array[3] = publickeyB[1]


    print(transfer_array)
    with open('transfer.txt', 'w') as file:
        for number in transfer_array:
            file.write(f"{number}\n")



"""
    numbers = [0,-1,-1]
    with open('personA.txt', 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

"""
print(" ------------------")
'''
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
'''