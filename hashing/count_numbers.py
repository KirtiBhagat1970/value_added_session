def count_numbers():
    arr=[1,2,1,3,2] #array elements
    max_val=max(arr) #maximum number in array
    hash_list=[0]*(max_val+1) #create hash list of 4 
                              #[0,0,0,0] max_val+1=3+1
    for num in arr:    
        hash_list[num]+=1
    
    # quries for how many times the this number appears
    queries=[1,4,7,2]
    for q in queries:
        if q<=max_val:
            print(f"number{q} appears {hash_list[q]}times")
        else:
            print(f"number{q} appears 0 times")

count_numbers()