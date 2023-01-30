def isUgly(n):
    array=[2,3,5]
    for item in array:
        while n%item==0:
            n//=item
    return n==1

isUgly(-2147483648)

