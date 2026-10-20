def highestOccurringElement(nums):
    # Write your code here
    
    max_count=0
    element=nums[0]
    
    
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count>max_count:
            max_count=count
            element=nums[i]
    return element
    
print(highestOccurringElement([1,2,2,3,3,3,4]))
