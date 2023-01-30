def moveZeros(nums):
    count=0
    i=0
    while i < len(nums):
        if nums[i]!=0:
            nums[count]=nums[i]
            count+=1
        i+=1
    while count < len(nums):
        nums[count]=0
        count+=1
    print(count)
    print(nums)
moveZeros([0])