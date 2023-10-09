# num = int(input("Enter a number: "))
# sum = 0
# n1 = len(str(num))
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** n1
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
n=int(input("Enter a number: "))
t=n
d=0
sum=0
while(n>0):
   d=d+1
   n=n//10
n=t
while(n>0):
   r=n%10
   sum=sum+r**d
   n=n//10
if(sum==t):
   print("armstrong")
else:
   print("not armstrong")         

