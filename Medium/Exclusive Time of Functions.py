# Exclusive Time of Functions
# O(n)
def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    res = [0 for _ in range(n)]
    stack = []
    prev_time = 0
    for log in logs:
        arr = log.split(":")
        fn, op, dt = int(arr[0]), arr[1], int(arr[2])
        if op == "start":
            if stack:
                res[stack[-1]] += dt - prev_time
            
            stack.append(fn)
            prev_time = dt
        else:
            last_fn = stack.pop(-1)
            res[last_fn] += dt - prev_time + 1
            prev_time = dt + 1
                    
    return res