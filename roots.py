number_1=float(input("enter the value of a: "))
number_2=float(input("enter the value of b: "))
number_3=float(input("enter the value of c: "))
a=((number_2**2)-(4*number_1*number_3))
if(a>0):
    print("real and distinct roots")
elif(a<0):
    print("imaginary roots")
else:
    print("the roots are real and same")
    root1=((-number_2)+(a**0.5))/2*number_1
    root2=((-number_2)-(a**0.5))/2*number_1
    print("the roots are",root1,root2)
    