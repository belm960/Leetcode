def removeDuplicate(nums,val):
    count=0
    i=0
    while i < len(nums):
        if nums[i]!=val:
            nums[count]=nums[i]
            count+=1
        i+=1
    print(count)
    print(nums)
    return count
removeDuplicate([0,1,2,2,3,0,4,2],2)