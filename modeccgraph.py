import matplotlib.pyplot as plt 
import numpy as np

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
    return sqrerootfinder(x** 3 - 5 * x + 5)
def linegen(Generator,point):
    grad = gradient(Generator,point)
    #print(grad)
    global prime
    x = []
    y = []
    yG = f(Generator)
    yintercept = (yG - Generator * grad) % prime
    for i in range(prime):
        x.append(i)
        y.append((yintercept + i*grad)%prime)
    return x,y

def linegen2(Generator,point):
    grad = gradient2(Generator,point)
    #print(grad)
    global prime
    x = []
    y = []
    yG = f(Generator)
    yintercept = (yG - Generator * grad) % prime
    for i in range(prime):
        x.append(i)
        y.append((yintercept + i*grad)%prime)
    return x,y

def gradient2(p1, p2):
    global prime
    y1 = f(p1)
    y2= add_inverse(f(p2))
    dx = (p2 - p1) % prime
    dy = (y2 - y1) % prime
    gradient = dy * mult_inverse(dx) % prime
    return gradient

def gradient(p1, p2):
    global prime
    y1 = f(p1)
    y2= f(p2)
    dx = (p2 - p1) % prime
    dy = (y2 - y1) % prime
    gradient = dy * mult_inverse(dx) % prime
    return gradient


def intersection(Generator, point, xline, yline,x1):
    for i in range(len(xline)):
        x = xline[i]
        if x != Generator and x != point:
            y = f(x)
            if y == yline[i]:
                return x,y
    print("fail")
    return intersection2(Generator, point, xline, yline,x1)

def intersection2(Generator, point, xline, yline,x1):
    for i in range(len(xline)):
        x = xline[i]
        if x != Generator and x != point and x in x1:
            y = add_inverse(f(x))
            if y == yline[i]:
                return x,y
    print("fail")
    return intersection(Generator, point, xline, yline,x1)
x1 = []
x2 = []
y1= []
y2 = []
#possible G, p1: 1,2,4,5,6,7,8,12,13,16,18,20,21,24
Generator = 33
point = 47
for i in range(prime):
    
    answer = f(i)
    if answer != None:
        x1.append(i)
        x2.append(i)
        y1.append(answer)
        y2.append(add_inverse(answer))
flag = True
for iterations in range(7):
    print("Generator, point",Generator,point)
    plt.scatter(x1, y1,s=10, color="orange")
    plt.scatter(x2, y2,s=10, color="blue")
    plt.scatter(Generator, f(Generator) ,s=20, color="red")
    plt.scatter(point, f(point) ,s=20, color="red")
    plt.show()
    fig, ax = plt.subplots()
    plt.scatter(x1, y1,s=10, color="orange")
    plt.scatter(x2, y2,s=10, color="blue")
    plt.scatter(Generator, f(Generator) ,s=20, color="red")
    plt.scatter(point, f(point) ,s=20, color="red")
    if flag:
        xline, yline = linegen(Generator,point) 
        px2, py2 = intersection(Generator,point, xline, yline,x1)
        flag = False
    else:
        xline, yline = linegen2(Generator,point) 
        px2, py2 = intersection2(Generator,point, xline, yline,x1)
        flag = True
    ax.plot(xline,yline,color = "blue",linestyle = "--")
    plt.scatter(px2, py2 ,s=30, color="green")
    plt.scatter(px2, add_inverse(py2) ,s=30, color="green")
    straightx = np.linspace(px2, px2,3)
    straighty = np.linspace(py2, add_inverse(py2),3)
    ax.plot(straightx, straighty, color='orange', linestyle='--')
    point = px2
    plt.show()
