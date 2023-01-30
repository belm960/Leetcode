def applyOperations(nums):
    i=0
    while i< len(nums)-1:
        if nums[i]==nums[i+1]:
            nums[i]*=2
            nums[i+1]=0
        i+=1
    while i < len(nums):
        if nums[i]!=0:
            nums[count]=nums[i]
            count+=1
        i+=1
    while count < len(nums):
        nums[count]=0
        count+=1
    return nums
    