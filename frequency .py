s=input("Enter a string:")
for i in s:
    frequency=s.count(i)
    print(str(i)+": "+str(frequency),end=", ")