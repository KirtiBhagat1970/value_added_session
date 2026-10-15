def reverseArray(arr):
    # Write your code here
    reverse=[]
    for i in range(len(arr)-1,-1,-1):
        reverse.append(arr[i])
    return reverse

    pass