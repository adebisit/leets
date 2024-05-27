# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
def setStr(haystack: str, needle: str):
    n = len(haystack)
    m = len(needle)
    
    flattened = []
    for i in range(n):
        for j in range(m):
            flattened.append(haystack[i] == needle[j])
    
    for i in range(n - m + 1):
        match = True
        _i = i
        for j in range(m):
            flat_i = (_i * m) + j
            match &= flattened[flat_i]
            _i += 1
        if match:
            return i
    return -1
    

if __name__ == "__main__":
    print(setStr("sadbutsad", "sad"))
    print(setStr("leetcode", "leeto"))
    print(setStr("mississippi", "issip"))
