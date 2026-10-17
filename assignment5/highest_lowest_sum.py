def sumOfFrequencies(arr):
    # Write your code here
    max_count=0
    low_count=len(arr)

    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
    
            if arr[i]==arr[j]:
                count+=1
            
        if count>max_count:
            max_count=count
            
        if count<low_count:
            low_count=count

    sum=max_count+low_count
    
    print(sum)
print(sumOfFrequencies([1,2,3,4,2,1,5,4,4]))
