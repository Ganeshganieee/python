num=int(input('enter a number:-'))
i=1
temp=False
while i<=num:
    if num%i==0  and i!=1 and i!=num:
        temp=Ture
    i+=1
if not temp:
    print(' num prime number')
else:
    print(' num not a prime number') 