# Number of Ways to Form a Target String Given a Dictionary
# O(n), O(n)
def numWays(self, words: List[str], target: str) -> int:
    dp = {}
    table = [[0] * 26 for _ in range(len(words[0]))]
    for i in range(len(words)):
        for j in range(len(words[0])):
            char = words[i][j]
            table[j][ord(char)-ord("a")] += 1
    def dfs(words_index, target_index) -> int:
        if target_index == len(target):
            return 1
        if words_index == len(words[0]):
            return 0
        if (words_index, target_index) in dp:
            return dp[(words_index, target_index)]
        count_ways = 0
        count_ways += dfs(words_index + 1, target_index)
        count_ways += table[words_index][ ord(target[target_index]) - ord("a") ] * dfs(words_index + 1, target_index + 1)
        dp[(words_index, target_index)] = int(count_ways % (1E9+7))
        return dp[(words_index, target_index)]
    return dfs(0, 0)