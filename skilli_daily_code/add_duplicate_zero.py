def duplicate_zero(arr):
    n=len(arr)
    result=[]
    for i in arr:
        if len(result)==n:
            break
        
        if i==0:
            result.append(0)
            if len(result)==n:
                break
            result.append(0)
        else:
            result.append(i)
            
    return result

result_zero=duplicate_zero([10,0,30,0,50,60])
print(result_zero)