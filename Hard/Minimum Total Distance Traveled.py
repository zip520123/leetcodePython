# Minimum Total Distance Traveled
# incorrect x
def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
    res = 0
    factory_map = {}
    for f, limit in factory:
        factory_map[f] = limit
    
    for r in robot:
        heap = []
        for f, limit in factory_map.items():
            if limit:
                distance = abs(f-r)
                heapq.heappush(heap, (distance, f))
        distance, f = heapq.heappop(heap)
        res += distance
        factory_map[f] -= 1
    
    return res

def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
    robot.sort()
    factory.sort()
    factories = []
    for f, limit in factory:
        for _ in range(limit):
            factories.append(f)
    
    dp = [[None for _ in range(len(factories)+1)] for _ in range(len(robot)+1)]

    def dfs(robot_index, factory_index) -> int:
        if dp[robot_index][factory_index] != None:
            return dp[robot_index][factory_index]

        if robot_index == len(robot):
            return 0
        if factory_index == len(factories):
            return math.inf
        
        
        select = abs(robot[robot_index]-factories[factory_index]
        ) + dfs(robot_index+1, factory_index+1)

        no_select = dfs(robot_index, factory_index+1)

        dp[robot_index][factory_index] = min(select, no_select)
        return dp[robot_index][factory_index]
    
    return dfs(0, 0)