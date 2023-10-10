n=int(input("Enter a number: "))
s1=0
s2=1
s3=1
c=0
if(n<=0):
    print("No. is less then zero")
elif(n==1):
    print(s1)    
else:
    while(n>=c):
        print(s1) 
        s4=s1+s2+s3
        s1=s2
        s2=s3
        s3=s4
        c=c+1 