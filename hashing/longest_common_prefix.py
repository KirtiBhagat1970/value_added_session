def longestCommonPrefix(str: list[str]) -> str:
    # Write your solution here
    if not str:
        return ""
    str.sort()
    first=str[0]
    last=str[-1]
    i=0
    while i<len(first) and i< len(last) and first[i]==last[i] :
        i+=1

    print( first[:i])

longestCommonPrefix(["flowers","fly","flow"])