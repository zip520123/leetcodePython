# Find Words That Can Be Formed by Characters
# O(n), O(n)
def countCharacters(self, words: List[str], chars: str) -> int:
    res = 0
    memo = defaultdict(int)
    for char in chars:
        memo[char] += 1
    for word in words:
        curr = copy.deepcopy(memo)
        is_valid = True
        for char in word:
            curr[char] -= 1
            if curr[char] == -1:
                is_valid = False
                break
        if is_valid:
            res += len(word)
    return res