def twoSum(nums,target):
    array=[]
    i=0
    while i < len(nums):
        j=i+1
        while j < len(nums):
            sum=nums[i]+nums[j]
            if sum==target:
                array.append(i)
                array.append(j)
            j+=1
        i+=1
    array.sort()
    return array
twoSum([2,7,11,15],9)