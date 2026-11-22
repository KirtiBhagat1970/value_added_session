def delete(arr,value):
    result=[]
    for i in arr:
        if i!=value:
            result.append(i)
    while len(result)<len(arr):
        result.append(0)
    return result
print(delete([10,20,30,10,10],10))