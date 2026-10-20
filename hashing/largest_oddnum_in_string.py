def largestOddNumber(s: str) -> str:
    # Write your solution here
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            print(int(s[:i+1]))
    return ""    
largestOddNumber("5347")