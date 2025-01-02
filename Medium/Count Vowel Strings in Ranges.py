# Count Vowel Strings in Ranges
# O(n), O(n)
def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    prefix = [0] * (len(words) + 1)
    for i in range(1, len(words) + 1):
        prefix[i] = prefix[i-1]
        if words[i-1][0] in "aeiou" and words[i-1][-1] in "aeiou":
            prefix[i] += 1
    res = []
    for start, end in queries:
        res.append(prefix[end+1]-prefix[start] )
    return res

def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    prefix = [0] * (len(words) + 1)
    for i in range(1, len(words) + 1):
        prefix[i] = prefix[i-1]
        if words[i-1][0] in "aeiou" and words[i-1][-1] in "aeiou":
            prefix[i] += 1
    
    return [prefix[end + 1] - prefix[start] for start, end in queries]