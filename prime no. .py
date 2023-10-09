n=int(input("enter a no. :"))
c=0
i=2
while(i<n):
    if(n%i==0):
        c=1 
        break
    i=i+1 
if(c==1):
        print("not prime")
else:
        print("prime")    