# Divide Players Into Teams of Equal Skill
# O(n log n), O(n)
def dividePlayers(self, skill: List[int]) -> int:
    arr = sorted(skill)
    n = len(arr)
    all_count = sum(arr)
    teams = n // 2
    skills_need = all_count // teams
    res = 0
    for i in range(n//2):
        if arr[i] + arr[n-1-i] != skills_need:
            return -1
        res += arr[i] * arr[n-1-i]
    return res