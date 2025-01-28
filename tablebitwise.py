'''Write a program to print truth table for bitwise operators( & , | and ^ operators)'''
print("a\tb\ta & b\ta | b\t a ^ b")
for a in [0, 1]:
    for b in [0,1]:
        print(a,"\t",b,"\t", (a&b), "\t",(a |b),"\t" , (a ^ b))