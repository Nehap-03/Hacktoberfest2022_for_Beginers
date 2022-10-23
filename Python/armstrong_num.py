a=int(input("Enter a number"))
d=a
l=len(str(a))
s=0
for i in range(l):
    s=s+((a%10)**l)
    a=a//10
if s==d:
    print(s," is Armstrong number")
else:
    print("Not an arstrong number")
