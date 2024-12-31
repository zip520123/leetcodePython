# Minimum Cost For Tickets
# O(1), O(1)
def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    dp = [ [0]*3 for _ in range(366) ]
    dp[0][0] = costs[0]
    for i in range(1, 8):
        dp[i][1] = costs[1]
    for i in range(1, 31):
        dp[i][2] = costs[2]
    travel_days = set(days)

    for day in range(1, 366):
        if day in travel_days:
            
            dp[day][0] = min(dp[day-1][0], dp[day-1][1], dp[day-1][2]) + costs[0]
            if day > 7:
                dp[day][1] = min(dp[day-7][0], dp[day-7][1], dp[day-7][2]) + costs[1]
            if day > 30:
                dp[day][2] = min(dp[day-30][0], dp[day-30][1], dp[day-30][2]) + costs[2]
        else:
            for i in range(3):
                if dp[day][i] == 0:
                    dp[day][i] = min(dp[day-1][0], dp[day-1][1], dp[day-1][2])
        
    return min(dp[-1])