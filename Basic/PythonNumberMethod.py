#Absolute Value
#Syntax is abs(10) Which is gives the absolute value. i.e. integer, float or complex number
# a=abs(10)
# b=abs(54.5)
# c=abs(-49.05)

# print(a,b,c)

## ceil method : it return ceiling value of the number x which we pass in argument. the ceiling value of a number x  will be the smallest integer not less than or equal to x. it gives the next number to the given number.

import math

a = math.ceil (-5.05)
print(a)

#floor method : it return floor value of the number x which we pass in argument. it gives lower number to the given number.

b = math.floor (5.95)
print(b)

#exponential method : will return a value of a number x which we pass in argument. i.e "e" raised to the power of x.

c = math.exp (3)
print(c)

## fabs() : it return the absolute value of the float number passed in argument.

d = math.fabs (10.5)
print(d)

## log(x) : it return natural logarithm of x, for x > 0.

e = math.log (65.5)
print(e)

## Max() : it return the largest item in an iterable or the largest of two or more arguments.

f = max(10,20,30,40,50)
print(f)

## Min() : it return the smallest item in an iterable or the smallest of two or more arguments.

g = min(10,20,30,40,50)
print(g)    

#pow(x,y) : it return the value of x raised to the power y.

h = pow(2,3)
print(h)

##sqrt(x) : it return the square root of x for x > 0. the negavtive number will return the value.

i = math.sqrt(64)
print(i)

#Trigonometric Functions

print(math.sin(90))
print(math.cos(90))

#hypot(x,y) : it return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).

j = math.hypot(2,3)
print(j)

#modf(x,y) : it return the value of x % y

k = math.fmod(20,3)
print(k)

