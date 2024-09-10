a="yes"
s=0
while(a=="yes"):
    n=int(input("enter a no "))
    if(n%2==1):
        s=s+n
        a=input("do u want ot enter a no (yes/no) ")
    else:
        a=input("do u want ot enter a no (yes/no) ")
print("sum of odd no = ",s)                                                                                                                                                                    