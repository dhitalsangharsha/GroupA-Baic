'''10) Given a list of numbers x = list(range(1, 20)). Loop over it using while loop and sum each numbers.
        Loop must terminate if the value of sum is greater than 34.'''

x=range(1,20)
sum=0
i=0
while i<len(x):
 sum=sum+x[i]
 i=i+1
 if sum>34:
      break

print(sum)

'''logic'''

x=range(1,20)
sum=0
i=0
while i<len(x):
 sum=sum+x[i]
 i=i+1
 if sum>34:
     print("Program terminated in "+str(i+1)+"th loop")
     break

print(sum)