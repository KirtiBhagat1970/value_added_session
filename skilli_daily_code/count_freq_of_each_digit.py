def count_freq(n):
    hash_list=[0]*10
    for ch in str(n):
        digit=int(ch)
        hash_list[digit]+=1
    return hash_list
print(count_freq(123256521))