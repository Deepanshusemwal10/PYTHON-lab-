'''Write a program to swap two numbers without taking additional variable'''
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
x, y = y, x 
print("After swapping: x and y are: ", x,y,"respectively")