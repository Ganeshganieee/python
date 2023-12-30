def add_int (var,i=0):
    if len(var)-1==i:
        if var[i]%2==0:
            return var[i]
        else:
            return 0
    if var[i]%2==0:
            return var[i]+add int(var,i+1)
    else:
            return add int(var,i+1)