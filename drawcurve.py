import matplotlib.pyplot as plt 
import numpy as np
curvecoef = [-5,5]
def f(x):
    global curvecoef
    ysquared=  x**3 + curvecoef[0]*x + curvecoef[1]
    valid = ysquared >= 0
    xvalid = x[valid]
    return xvalid, np.sqrt(ysquared[valid])

def singlef(x):
    global curvecoef
    ysquared=  x**3 + curvecoef[0]*x + curvecoef[1]
    if ysquared < 0:
        return -1
    else:
        return np.sqrt(ysquared)


startingx = -2.5
startingy = singlef(startingx)

secondx = -1.1
secondy = singlef(secondx)


def line(x,point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    gradient = (y2-y1)/(x2-x1)
    return x, (x-x1) * gradient + y1
def line2(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    gradient = (y2-y1)/(x2-x1)
    y_intercept = -x1 * gradient + y1
    return gradient, y_intercept


def intersection(gradient,y_intercept,startingx,secondx):
    global curvecoef
    acutalcoef = [1,-(gradient ** 2),curvecoef[0]-2*gradient*y_intercept, curvecoef[1]-(y_intercept**2)]
    roots =  np.roots(acutalcoef)

    #redo later
    for i in roots:
        print("roots ",i)

    filtered_roots = [root for root in roots if not np.isclose(root, startingx) and not np.isclose(root, secondx)]
    print("filtered roots: ", filtered_roots)
    
    return filtered_roots[0],singlef(filtered_roots[0])
    
def intersection2(gradient,y_intercept,secondx):
    global curvecoef
    acutalcoef = [1,-(gradient ** 2),curvecoef[0]-2*gradient*y_intercept, curvecoef[1]-(y_intercept**2)]
    roots = np.roots(acutalcoef)

    #redo later
    for i in roots:
        print("roots: ",i)
    print("secondx:",secondx)

    filtered_roots = [root for root in roots if not np.isclose(root, secondx)]
    print("filtered root: ",filtered_roots[0])
    return filtered_roots[0],singlef(filtered_roots[0])


for n in range(1,9):
    fig, ax = plt.subplots()

    x = np.linspace(-3, 9, 10000)  # Sample data.

    newx,newy = f(x)
    line_x,line_y = line(x,(startingx, startingy), (secondx, secondy))

    gradient, y_intercept = line2( (startingx, startingy), (secondx, secondy))
    xvalue,yvalue = intersection(gradient,y_intercept,startingx,secondx) 

    data1= [startingx,secondx]
    data2= [startingy,secondy]
    pointdata1 = [xvalue,xvalue]
    pointdata2 = [yvalue,-yvalue]
    straighty = np.linspace(-yvalue,yvalue,3)
    xvalues = np.linspace(xvalue,xvalue,3)


    ax.plot(xvalues, straighty, color='orange', linestyle='--')

    
    secondline_x, secondline_y = line(newx, (startingx, startingy), (xvalue, -yvalue))


    ax.scatter(data1, data2)
    ax.scatter(pointdata1,pointdata2)


    ax.plot(line_x, line_y, label='Line through points', color='blue', linestyle='--')

    # Plot the elliptic curve
    ax.plot(newx,newy, label='Elliptic curve (positive)')
    ax.plot(newx, -(newy), label='Elliptic curve (negative)')

    # Customize plot
    ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
    ax.axvline(0, color='gray', linewidth=0.8, linestyle='--')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_title('Elliptic Curve')

    ax.plot(secondline_x, secondline_y, label='Second line through points', color='red', linestyle='--')
    
    secondgradient,secondy_intercept = line2((startingx, startingy), (xvalue, -yvalue))
    secondxvalue, secondyvalue = intersection(secondgradient,secondy_intercept,startingx,xvalue) #secondgradient,secondy_intercept,xvalue

    print("xvalue",xvalue)
    print("gradient, y intercept", secondgradient, secondy_intercept)
    print("yvalue", secondgradient*xvalue+secondy_intercept)



    straighty2 = np.linspace(secondyvalue,-secondyvalue,3)
    straightx2 = np.linspace(secondxvalue,secondxvalue,3)
    
    ax.scatter(secondxvalue, secondyvalue)
    ax.scatter(secondxvalue, -secondyvalue)
    ax.plot(straightx2, straighty2, color='orange', linestyle='--')

    # Show the plot

    #startingx = secondx
    #startingy = singlef(startingx)

    secondx = secondxvalue
    secondy = singlef(secondxvalue)
    print("second x", secondx, n)
    print()
    plt.show()
