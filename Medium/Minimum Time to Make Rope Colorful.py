# Minimum Time to Make Rope Colorful
# O(n),O(n)
def minCost(self, colors: str, neededTime: List[int]) -> int:
    res = 0
    stack = []
    for i in range(len(colors)):
        if stack:
            (last_color, last_time) = stack.pop(-1)
            if last_color == colors[i]:
                if last_time < neededTime[i]:
                    res += last_time
                    stack.append((colors[i], neededTime[i]))
                else:
                    res += neededTime[i]
                    stack.append((colors[i], last_time))
            else:
                stack.append((colors[i], neededTime[i]))
        else:
            stack.append((colors[i], neededTime[i]))
    return res

# O(n), O(1)
def minCost(self, colors: str, neededTime: List[int]) -> int:
    res = 0
    curr_color_index = 0
    n = len(colors)
    for i in range(1,n):
        if colors[i] == colors[curr_color_index]:
            if neededTime[i] < neededTime[curr_color_index]:
                res += neededTime[i]
            else :
                res += neededTime[curr_color_index]
                curr_color_index = i
        else:
            curr_color_index = i
    return res