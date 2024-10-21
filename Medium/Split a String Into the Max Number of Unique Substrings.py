# Split a String Into the Max Number of Unique Substrings
# O(2^n), O(n)
def maxUniqueSplit(self, s: str) -> int:
    seen = set()

    def dfs(index) -> int:
        if index == len(s):
            return 0

        max_count = 0

        for i in range(index, len(s)):
            sub_string = s[index: i+1]
            if sub_string not in seen:
                seen.add(sub_string)
                max_count = max(max_count, 1 + dfs(i+1))
                seen.remove(sub_string)
        return max_count
    return dfs(0)