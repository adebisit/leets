from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]
    for _str in strs:
        tempPrefix = ""
        for i in range(len(_str)):
            if i == len(prefix) or prefix[i] != _str[i]:
                break
            tempPrefix += _str[i]
        prefix = tempPrefix
    return prefix