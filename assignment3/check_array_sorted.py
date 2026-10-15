def isArraySorted(arr):
    # Write your code here
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                return False
    return True
    
    pass