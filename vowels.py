s=input("Enter a string:")
vcount=0
ccount=0
s=s.lower()
for i in range(0,len(s)):
    if s[i] in('a','e','i','o','u'):

      if s[i]>='a'and[i<='z']:
        ccount=ccount+1
        print("total vowel and consonant")
        print(vcount)
        print(ccount)