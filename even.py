#wap toall even number form 1 to5- by using loop
num= int(input(' '))
temp=False
for i in range(2,num):
    if num%i==0:
         temp=Ture
if  not temp:
      printt('prime')
else:
    print('it is not prime')