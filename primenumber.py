#wap to check wheather gievn number is prime number or not
num=int(input('enter a number:-'))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(' num prime number')
else:
    print(' num not a prime number')        