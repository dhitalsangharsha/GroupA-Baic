'''13) Given a list of strings x = ["Hello", "my", "name", "is", "John Cena"]. Write a python program
to produce a full length string: "Hello my name is John Cena"
For example:
input: ["Hello", "my", "name", "is", "John Cena"]
output: "Hello my name is John Cena"'''

x=["Hello","my","name","is","John Cena"]
for i in x:
    print("{} ".format(i),end="")