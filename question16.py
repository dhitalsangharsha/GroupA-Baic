'''16) Convert the code snippet given below to list comprehension to get the exact result.
my_list = []
for x in [20, 40, 60]:
for y in [2, 4, 6]:
my_list.append(x * y)
print(my_list) # Output: [40, 80, 120, 80, 160, 240, 120, 240, 360]'''

x=[20,40,60]
y=[2,4,6]

my_list=[i*j for i in x for j in y]
print(my_list)