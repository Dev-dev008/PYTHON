n=int(input("enter a no.: "))
rev=0
t=n
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(rev==t):
    print("palindrome") 
else:
    print("not palindrome")       