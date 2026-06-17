# Determine if Two Strings Are Close
# O(n), O(n)
def closeStrings(self, word1: str, word2: str) -> bool:
    set1, set2 = set(word1), set(word2)
    if set1 != set2: return False

    memo1, memo2 = defaultdict(int), defaultdict(int)
    for char in word1:
        memo1[char] += 1
    for char in word2:
        memo2[char] += 1
    
    memo3, memo4 = defaultdict(int), defaultdict(int)
    for _, val in memo1.items():
        memo3[val] += 1
    for _, val in memo2.items():
        memo4[val] += 1
    return memo3 == memo4

# O(n + M + klog k), O(1)
def closeStrings(self, word1: str, word2: str) -> bool:
    arr1 = [0] * 26
    arr2 = [0] * 26
    set1 = set()
    set2 = set()
    for char in word1:
        arr1[ord(char)-ord('a')] += 1
        set1.add(char)
    for char in word2:
        arr2[ord(char)-ord('a')] += 1
        set2.add(char)
    arr1.sort()
    arr2.sort()
    return arr1 == arr2 and set1 == set2

# O(n), O(1)
def closeStrings(self, word1: str, word2: str) -> bool:
    arr1 = [0] * 26
    arr2 = [0] * 26
    set1 = set()
    set2 = set()
    for char in word1:
        arr1[ord(char)-ord('a')] += 1
        set1.add(char)
    for char in word2:
        arr2[ord(char)-ord('a')] += 1
        set2.add(char)
    memo1, memo2 = defaultdict(int), defaultdict(int)
    for val in arr1:
        memo1[val] += 1
    for val in arr2:
        memo2[val] += 1
    return memo1 == memo2 and set1 == set2