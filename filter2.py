# wap to flter all single value date item in a given hetogenous list in the collection
def sample(a):
    if a%5==0 and a%3==0:
        return True
    else:
        return False
out=filter(sample,range(1,201))
print(list(out))