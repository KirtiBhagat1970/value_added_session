def isIsomorphic(s: str, t: str) -> bool:
    # Write your solution here
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s.index(s[i]) != t.index(t[i]):
            return False
    return True
print(isIsomorphic("egg","add"))