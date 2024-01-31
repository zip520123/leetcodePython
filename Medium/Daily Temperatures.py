# Daily Temperatures
# O(n), O(n)
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    res = []
    n = len(temperatures)
    for i in range(n-1, -1, -1):
        curr = temperatures[i]
        while stack and temperatures[stack[-1]] <= curr:
            stack.pop(-1)
        if stack: 
            res.insert(0, stack[-1] - i)
        else:
            res.insert(0, 0)
        stack.append(i)
    return res
