def findLcm(n1, n2):
    # Write your code here
    #find the largest number between n1 and n2
    if n1>n2:
        lcm=n1
    else:
        lcm=n2
    
    #run the for loop from n1*n2
    for i in range(1,n1*n2):
        #if lcm is divisible  by both numbers
        if lcm%n1==0 and lcm%n2==0:
            #if yes break the loop
            break
        #else increase lcm by 1
        lcm=lcm+1
    return lcm
            
        

    pass