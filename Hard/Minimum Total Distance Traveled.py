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

# O(n^2*m)
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

# O(n^2*m), O(n*m)
def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
    robot.sort()
    factory.sort()
    factories = []
    for f, limit in factory:
        for _ in range(limit):
            factories.append(f)
    dp = [ [0 for _ in range(len(factories)+1)] for _ in range(len(robot)+1) ]
    for i in range(1, len(robot)+1):
        dp[i][0] = math.inf
    
    for r in range(1, len(robot)+1):
        for f in range(1, len(factories)+1):
            dp[r][f] = min(dp[r-1][f-1] + abs(factories[f-1] - robot[r-1]),
                dp[r][f-1]
            )

    return dp[-1][-1]

'''   factories
        0  1  2 
      0 0  0  0
robot 1 x  1  1
      2 x  x  2

robot = [-1,1] , factories = [-2, 2]
f(factory, robot) = min(f(factory-1, robot-1) + abs(factory-robot), f(factory-1, robot))
'''