a=float(input("enter first no"))
b=float(input("enter second no"))
c=float(input("enter third no"))
d=float(input("enter four no"))
if (a>b and a>c and a>d):
        print("greatest no is:",a)
elif (b>c and b>d):
        print("greatest no is:",b)
elif(c>d):
        print("greatest no is:",c)
elif(d>c):
        print("greatest no is:",d)
else:
        print("either any two values or all the four values are equal")        