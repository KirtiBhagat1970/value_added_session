def secondHighestOccurringElement(arr):
    # Write your code here
    max_count=0
    second_count=0
    element=arr[0]
    second_element=arr[0]
    for i in range(len(arr)):#for select element in arr

        count=0
        for j in range(len(arr)):#for count occurences
            if arr[i]==arr[j]:
                count+=1
        
        if count>max_count:
            second_count=max_count
            second_element=element

            max_count=count
            element=arr[i]
        elif count<max_count and count>second_count:
            second_count=count
            second_element=arr[i]
    print(second_element)  
      
print(secondHighestOccurringElement([1,2,3,2,4,2,3]))