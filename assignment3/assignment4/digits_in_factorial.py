def digitsInFactorial(n: int) -> int:
    # Write your solution here
    # fact=1
    # for i in range(1,n+1):
    #     fact=fact*i
    # return len(str(fact))

    # seccond approach
    fact=1
    count=0
    for i in range(1,n+1):
        fact=fact*i
    while fact>0:
        count+=1
        fact=fact//10
    print (count)

digitsInFactorial(5)

