'''8) Write a Python function that solves the linear equation (y=mx+c). Here, (variable) x is arbitary
value that is taken from the user and (slope) m is 0.5 and y-intercept (c) is 2.5.'''

x=float(input("enter the x coordinate:"))
m=0.5
c=2.5
y=m*x+c
print("the value of y intercept is {} of slope {} and constant {}".format(y,m,c))