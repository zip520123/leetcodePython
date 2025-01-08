# Count Prefix and Suffix Pairs I
# O(n^2) time O(1) space
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res

def isPrefixAndSuffix(s1, s2):
    return isPrefix(s1, s2) and isSuffix(s1, s2)

def isPrefix(s1, s2):
    if len(s1) > len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
def isSuffix(s1, s2):
    if len(s1) > len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[len(s2)-len(s1)+i]:
            return False
    return True
