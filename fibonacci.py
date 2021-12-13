
n=int(input("Enter limit"))
if(n<0):
    print("No. should be 0 or greater than 0")
n1=0
n2=1
sum=0
for i in range(n):
    print(sum, end=" ")
    n1=n2
    n2=sum
    sum=n1+n2
    
