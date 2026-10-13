def isPerfectNumber(n):
    # Write your code here

    sum=1
    # i runs from 2 to square root of n+1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            sum=sum+i
            sum+=n//i
    
    return sum==n
