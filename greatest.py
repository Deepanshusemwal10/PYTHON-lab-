num1= int (input ("Enter the first number:"))
num2= int (input ("Enter the second number:"))
num3= int (input ("Enter the third number:"))
if num1>num2:
    if num1>num3:
        print(num1,"num1 is greater")
    elif num3>num1:
        print(num3,"num3 is greater")
    elif num2>num1:
        if num2>num3:
            print(num2,"num2 is greater")
        elif num3>num2:
            print(num3,"num3 is greater")
            