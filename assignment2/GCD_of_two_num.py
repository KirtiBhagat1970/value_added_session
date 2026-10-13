def gcdOfTwoNumbers(n1, n2):
    # Write your code here
    #first find the smallest number between n1 and n2
    if n1<n2:
        smallest=n1
    else:
        smallest=n2
    

    gcd=0
    for i in range(1,smallest+1):
        if n1%i==0 and n2%i==0:
            #store common divisor
            gcd=i

    return gcd

    pass