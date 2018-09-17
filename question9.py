'''9) Write a function that can accept N number of integer arguments and produce a sum of those
numbers.'''
def numbers():
    n=int(input("how many numbers you want to enter to find sum ?\n"))
    sum=0
    for i in range(1,n+1):
        s=int(input("enter no. {}:".format(i)))
        sum+=s
    print("the total sum of given numbers is:",sum)
numbers()

