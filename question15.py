'''15) Given a list of numbers my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. Write a list comprehension to
       produce squared value of odd numbers only from the list my_numbers.'''

my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_squares = [n**2 for n in my_numbers if n%2!=0]
print(odd_squares)