def isArraySorted(arr):
    # Write your code here
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
    pass