'''7) Write a python script to demonstrate at least 10 built in functions in Python.'''

print("enter the intiger list items seperated by space")
l= [int(x) for x in input().split()]
print("your list is created as:",l)

#to find the length of above list we use len function
print("toral no. of items in the given list is:",len(l))

#sort fun. is used to sort the list is ascending order
l.sort()
print("above list in sorted form is given by:",l)

#find the absolute value
n=int(input("enter the no. of whih you want to find absolute value:"))
print("absolute value of {} is {}".format(n,abs(n)))

