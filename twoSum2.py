def twoSum(numbers,target):
    array=[]
    i=0
    get = False
    while i < len(numbers):
        if numbers[i]>target:
            break
        else:
            j=i+1
            while j<len(numbers) and (numbers[j]< target or target == numbers[j]):
                get = False
                if numbers[i]+numbers[j] == target:
                    array.append[j+1]
                    get=True
                j+=1
            if get==True:
                array.append(i+1)
        i+=1                
                
        