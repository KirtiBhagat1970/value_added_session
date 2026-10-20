def character_count():
    str="abcdefgadbc"
    hash_list=[0]*26
    for char in str:
        hash_list[ord(char)-ord("a")]+=1
    
    queries=["a","b","d","f"]
    for q in queries:
        count=hash_list[ord(q)-ord("a")]
        print(f"character {q} apperas:{count} times")
character_count()