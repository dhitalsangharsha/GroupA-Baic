'''11) Write a simple Python program to demonstrate the use of conditions (if-elif-else)'''


'''I had created the progrom to check the gender'''

def invalid():
    print("Invalid entry")
def checker():
    c = input("if you are attracted to Male then press Y  press N if you are attracted to Female")
    return c
def Male():
    c=checker()
    if c.lower()=='y':
        print("you are a gay")
    elif c.lower()=='n':
        print("you are male")
    else:
        invalid()

def Female():
    c=checker()
    if c.lower() == 'y':
        print("you are a Woman")
    elif c.lower()=='n':
        print("you are Lesbian")
    else:
        invalid()

print("\nchek your gender\n")
ch=input("enter Y if you have male genetile if no then press N \n")

if ch.lower()=='y':
    Male()
elif ch.lower()=='n':
    Female()
else:
    invalid()



