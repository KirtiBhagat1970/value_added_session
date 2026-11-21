def count_digit(n,k):
    hash_list=[0]*10
    for ch in str(n):
        digit=int(ch)
        hash_list[digit]+=1
    
    result=[]
    for i in range(10):
        if hash_list[i] >=k:
            result.append(i)
            
    return result

print(count_digit(123123456,2))
        