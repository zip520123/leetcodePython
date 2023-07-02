# Maximum Number of Achievable Transfer Requests
# O(n*requests.len), O(n+requests.len)
def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
    arr = [0] * n

    def dfs(index: int, count: int) -> int:
        if index == len(requests):
            for num in arr:
                if num != 0:
                    return 0
            return count
        res = 0
        request = requests[index]
        arr[request[0]] -= 1
        arr[request[1]] += 1
        res = max(res, dfs(index+1, count+1))
        arr[request[0]] += 1
        arr[request[1]] -= 1
        res = max(res, dfs(index+1, count))
        return res
    return dfs(0,0)