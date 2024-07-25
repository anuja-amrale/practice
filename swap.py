print("Enter two numbers")
a=input("Enter 1st no:")
b=input("Enter 2nd no:")
t=a
a=b
b=t
print(a,b)

#another method
a,b=b,a
print(a,b)