def fname(a):
    if a%2==0:
        return True
    else:
        return False
out=filter (fname,[2,4,6,1,3,7,9,4,3])
print(list(out))