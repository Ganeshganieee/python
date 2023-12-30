#wap to check given number is prefect number
a=int(input('enter number'))
out=0
for i in range(1,a):
    if a%i==0:
        out=out+i
if out==a:
    print('pefect number')
else:
    print('not a prefcet number')