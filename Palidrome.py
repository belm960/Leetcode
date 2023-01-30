def palindrome(x):
    numstring=str(x)
    i=0
    j=len(numstring)-1
    value=True
    while i<j:
        if numstring[i]!=numstring[j]:
            value = False
        i+=1
        j-=1
    return value