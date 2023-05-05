# Maximum Number of Vowels in a Substring of Given Length
# O(n) time, O(1) space
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0;r=0;res=0; currVowel=0
        while r<len(s):
            if isVowel(s[r]):
                currVowel += 1
            if r-l+1>k:
                if isVowel(s[l]):
                    currVowel -= 1
                l += 1
            res = max(res, currVowel)
            r += 1
        return res

def isVowel(char) -> bool:
    vowels = ["a", "e","i","o","u"]
    return char in vowels