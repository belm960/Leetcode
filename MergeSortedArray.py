def removeDuplicates(nums):
    i=1
    memory = 1
    memory1 = 0
    array=[]
    array.append(nums[0])
    while i< len(nums):
        if nums[i]!=nums[i-1]:
            array.append(nums[i])
            memory+=1
        elif nums[i]==nums[i-1]:
            if memory1 != nums[i]:
                memory1 =  nums[i]  
        i+=1
    nums=array
    print(memory)
    print(nums)
    return memory

removeDuplicates([1,1,2])
