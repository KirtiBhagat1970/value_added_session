def findDivisors(n):
    # Write your code here
    #create a empty list to store divisors
    result=[]
    

    for i in range(1,n+1):
        if n%i==0:
            #if number is divisor of i it append the number in result list
            result.append(i)
    
    return result

    pass