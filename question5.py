'''5) Take an arbitrary input string from user and print it 10 times.'''
string=input("enter a string:")
print("\nprinting  {} 10 times ".format(string))
for i in range(1,11):
    print(str(i)+':',string)