# Find the Number of Distinct Colors Among the Balls
# O(n), O(n)
def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    res = []
    count = 0
    color_count = defaultdict(int)
    ball_color = defaultdict(int)
    for ball, color in queries:
        if ball_color[ball] != 0:
            curr_color = ball_color[ball]
            color_count[curr_color] -= 1
            if color_count[curr_color] == 0:
                count -= 1
        ball_color[ball] = color
        color_count[color] += 1
        if color_count[color] == 1:
            count += 1
        res.append(count)
    return res