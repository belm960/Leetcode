def reverse(x):
    newx = str(x)
    i=0
    sum = 0
    mul=1
    value=False
    while i<len(newx):
        sum+=(int(newx[i])*mul)
        mul*=2           
        i+=1
    n=sum
    print(n)
    return sum
reverse(11111111111111111111111111111101)