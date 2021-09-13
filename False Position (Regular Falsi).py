import math
import os
#from numpy.linalg import *
## 2*(3**(1/2))*math.sin(x) - 20*(math.cos(x)) + 5
## episilon = 0.001
## a = 0, b = (math.pi/2)

#User Input Equation
print("To enter some maths function, math.cos(x), math.pi, math.log(x), 5**2 = 5^2, 5*2 = 5 times 2, 5/2 = 5 divided by 2\n")
equation = input("Enter your equation only in terms of x: ")

#Determine suitable initial value
valid_Initial_Values = False

#fa and fb must be opposite sign to indicate that this line cuts the x axis, postive multiply negative gives a value < 0
while valid_Initial_Values == False:
    #Find fa

    a = eval(input("Enter a: "))
    x = a

    fa = eval(equation)

    #find fb

    b = eval(input("Enter b: "))
    x = b

    fb = eval(equation)

    #Check if fa and fb are opposite signs
    product = fa*fb
    print("Value of fa:", fa)
    print("Value of fb:", fb)
    if product >= 0:
        print("Invalid Initial Values. Please Input Again!")
    else:
        valid_Initial_Values = True

#Enter TOL or Known As Convergence Tolerance
TOL = input("Enter TOL (Convergence Tolerance): ")
#TOL = "{0:.20f}".format(eval(TOL)).rstrip("0")

#Get Number of Decimal Places According to TOL
dp = str(TOL)[::-1].find('.')
dp = dp + 1

#Enter Number Of Iterations
N = eval(input("Number of Iterations: "))


#Initialise Iteration
i = 1

print("n".center(10), "a".center(17), "b".center(15), "x".center(15), "f(x)".center(22), "f(a)".center(20), "f(b)".center(20))
print("="*120)

while i <= N:
    #Formula
    
    x = (a*fb - b*fa)/(fb-fa)
    
    #x = a - ((b - a)* fa)/(fb - fa) Can be simplified into this
        
    if abs(x-a) < eval(TOL) or abs(b-x) < eval(TOL):
        print(str(i).center(10), str(format(a, '.'+ str(dp) + 'f')).center(15), str(format(b, '.'+ str(dp) + 'f')).center(15),
            str(format(x, '.'+ str(dp) + 'f')).center(15), str(format(fx, '.'+ str(dp) + 'E')).center(25),
              str(format(fa, '.'+ str(dp) + 'f')).center(20),str(format(fb, '.'+ str(dp) + 'f')).center(20))
        
        print("\nThe method is succesful after " + str(i) + " iterations")
        print("The Approximate Root To " + str(dp-1) + " Decimal Places Is " + str(format(x, '.'+ str(dp-1) + 'f'))+ " From Rounding Up/Down " + str(format(x, '.'+ str(dp) + 'f')))
        break
    
    #Calculate f(x) when x is the current value, as more iteration is done, f(x) approaches 0
    fx = eval(equation)

    print(str(i).center(10), str(format(a, '.'+ str(dp) + 'f')).center(15), str(format(b, '.'+ str(dp) + 'f')).center(15),
            str(format(x, '.'+ str(dp) + 'f')).center(15), str(format(fx, '.'+ str(dp) + 'E')).center(25),
              str(format(fa, '.'+ str(dp) + 'f')).center(20),str(format(fb, '.'+ str(dp) + 'f')).center(20))
    
    i = i + 1
    
    #This makes it different from the Secant Method as This Ensure Convergance Between The Interval a,b
    #same sign indicating that it is squeezing from the left to right, f(b) and f(x) or f(c) has opposite sign
    if fa*fx > 0:
        #new a value for next iteration
        a = x
        #new fa value for next iteration
        fa = fx 
    #opposite sign indicating that it is squeezing from right to left, f(a) and f(x) or f(c) has opposite sign
    else:
        #new b value for next iteration
        b = x
        #new fb value for next iteration
        fb = fx
    

if (i-1 == N) and ((abs(x-a) > eval(TOL) or abs(b-x) > eval(TOL))):
        print("\nThe Method Failed After " + str(i-1) + " Iterations")

os.system("pause")
##'.'+ str(dp) + 'f' or '.nf', where n is the number of decimal places, this formatting truncates and rounds up the number

