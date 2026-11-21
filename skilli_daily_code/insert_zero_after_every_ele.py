def insert_ele(arr):
    result=[]
    for i in arr:
        if len(result)<len(arr):
            result.append(i)
        if len(result)<len(arr):
            result.append(0)
    return result
print(insert_ele([10,20,30,40]))