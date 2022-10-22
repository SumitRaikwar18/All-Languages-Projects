num=int(input("ENTER 3 DIGIT NUMBER :-"))
f=num
sum=0
while(f>0):
    a=f%10
    f=int(f/10)
    sum=sum+(a**3)
if (sum==num):
    print(" IT IS A ARMSTRONG NUMBER ",num)
else:
    print(" IT IS NOT A ARMSTRONG NUMBER ",num)
