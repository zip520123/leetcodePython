# Find Players With Zero or One Losses
# O(n log n), O(n)
def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    memo = defaultdict(int)
    players = set()
    for winner, loser in matches:
        memo[loser] += 1
        players.add(winner)
        players.add(loser)
    notLosts = []
    oneLosts = []
    for player in players:
        if memo[player] == 0:
            notLosts.append(player)
        if memo[player] == 1:
            oneLosts.append(player)
    return [sorted(notLosts), sorted(oneLosts)]