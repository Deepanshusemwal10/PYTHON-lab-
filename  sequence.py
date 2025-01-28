''' Using membership operator find whether a given number is in sequence
(10,20,56,78,89)'''
number = int(input("Enter a number: "))
sequence = (10, 20, 56, 78, 89)
if number in sequence:
    print(number, " is in the sequence.")
else:
    print(number," is not in the sequence.")