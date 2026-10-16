def reverseArray(arr):
    # Write your code here
    result=[]
    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
    return result
    pass