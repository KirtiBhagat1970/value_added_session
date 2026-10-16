def countOddNumbers(n, array):
    # Write your code here
    count=0
    for i in range(n):
        if array[i]%2!=0:
            count+=1       
    return count

    pass