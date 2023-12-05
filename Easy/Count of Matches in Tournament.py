# Count of Matches in Tournament
# O(log n), O(1)
def numberOfMatches(self, n: int) -> int:
    matches = 0
    teams = n
    while teams > 1:
        nextTeams = teams // 2
        matches += teams // 2
        if teams % 2 == 1:
            nextTeams += 1
        teams = nextTeams
    return matches
        