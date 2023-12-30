'''a='xyz'
b='abc'
out=''
for i in range(len(a)):
    out+=a[i]+b[i]
print(out)'''

'''a='xyz'
b='abc'
out=''
for i,j in zip (a,b):
    out=out+i+j
print(out)'''

'''a='xyz'
b='abc'
out=''
for i in zip (a,b):
    print(i)'''

'''a=['j','s','d']
b=['a','b','c']
c=['W','W','W']
out=''
for i,j,k in zip (a,b,c):
    out=out+i+j+k
    print(out)'''
'''a=[1,2,3]
b=[6,5,5]
c=[9,0,0]
out=[]
for i,j,k in zip (a,b,c):
    out=out+[i]+[j]+[k]
    print(out)'''

'''a='ABC'
b=[4,5,6]
out={}
for i,j in zip (a,b):
    out[i]=j
print(out)'''

''''a='ABC'
b=[4,5,6]
out={}
for i,j in enumerate(a):
    print(i,j)'''
'''a="abcd"
out=''
for i,j in enumerate(a):
    out=out+j+str(i)
print(out)'''


from funtools import reduce
a=[1,2,3,4]
out=reduce(add,a)
print(out)














print(out)